import numpy as np
import hicstraw as hs
import pandas as pd
import sys

import tensorflow as tf

from hicml.DataStructures import LockedList
from concurrent.futures import ThreadPoolExecutor,as_completed

print("hic-straw", hs.__version__)
FEATURE_KEY = 'feat_resolution'
CHROM_KEY = 'chr1'
X1_KEY = 'x1'
X2_KEY = 'x2'
Y1_KEY = 'y1'
Y2_KEY = 'y2'


def find_resolutions_from_list(df):
    df[FEATURE_KEY] = df[X2_KEY] - df[X1_KEY]
    # print('Feature list contains the following resolutions:', df[FEATURE_KEY].unique())
    return df[FEATURE_KEY].unique()


def make_resolution_sub_lists(df):
    if '#chr1' in df.columns:
        df.rename(columns={'#chr1': CHROM_KEY}, inplace=True)
    df = df.sort_values(FEATURE_KEY)
    groups = df.groupby(FEATURE_KEY)
    dct = {name: group for name, group in groups}
    return dct


def round_by_res(value, resolution):
    return (value // resolution) * resolution


def make_region(coordinates, width: int, resolution: int):
    (chrom1, x1, x2, y1, y2) = coordinates
    mid_x = round_by_res(x1 + ((x2 - x1) // 2), resolution)
    mid_y = round_by_res(y1 + ((y2 - y1) // 2), resolution)

    half_width = (width // 2) * resolution
    cx1 = mid_x - half_width
    cx2 = mid_x + half_width
    cy1 = mid_y - half_width
    cy2 = mid_y + half_width
    return cx1, cx2, cy1, cy2


class Oracle:
    def __init__(self, loop_list_path: str,
                 hic_file: str, models_dir: str, norm: str,
                 stem:str, num_straw_workers:int, output_dir:str, width: int = 56, chr_list: list = None):
        self.__loopList = self.load_loops(loop_list_path)
        self.__hic = hs.HiCFile(hic_file)
        self.__norm = norm
        self.__width = width
        self.__oracleList = LockedList()
        self.__modelsDir = models_dir
        self.__resolutions = sorted(find_resolutions_from_list(self.__loopList))
        self.__stem = stem
        self.__numWorkers = num_straw_workers
        self.__outputDir = output_dir
        self.__resolution_sub_lists = make_resolution_sub_lists(self.__loopList)
        self.__chr = self.make_chr_list(chr_list)
        self.__model = tf.keras.models.load_model(self.__modelsDir)

    def make_chr_list(self, chr_list):
        if chr_list is None:
            return [x.name for x in self.__hic.getChromosomes() if x.name != 'All']
        return [str(x) for x in chr_list]

    @staticmethod
    def load_loops(loop_list):
        df = pd.read_csv(loop_list, sep="\t")
        if '#chr1' in df.columns:
            df.rename(columns={'#chr1': CHROM_KEY}, inplace=True)
        # df = df[~df['#chr1'].str.contains("#")]
        df = df.astype({X1_KEY: int, X2_KEY: int, Y1_KEY: int, Y2_KEY: int})
        return df

    @staticmethod
    def preprocess(matrix, scale=0.1):
        if np.sum(matrix) < 1e-9:
            return matrix
        flattened_data = matrix.flatten()
        flattened_data = flattened_data[flattened_data > 0]
        median_val = np.median(flattened_data)
        mad_val = np.median(np.abs(flattened_data - median_val))
        if mad_val == 0:
            return matrix
        m = np.tanh(scale * (matrix - median_val) / mad_val)
        return (m - m.min()) / (m.max() - m.min())


    def makePredictions(self,chr):
        # scores=[]
        df_tmp = self.__loopList[self.__loopList['chr1']==chr]
        df_tmp = df_tmp.reset_index(drop=True)
        if df_tmp.shape[0]==0:
            return f'{chr} does not have any loops.'
        batch = np.zeros((len(df_tmp),self.__width,self.__width,1))
        for reso in self.__resolutions:
          # print ('ORACLE is running at', reso, 'kb', 'on chr', chr, flush = True)
          print (f'ORACLE is running at {reso} on {chr}', flush=True)
          mzd = self.__hic.getMatrixZoomData(chr, chr, "observed", self.__norm , "BP", reso)
          for i, row in df_tmp.iterrows():   
            x1,x2,y1,y2 = make_region((row['chr1'],row['x1'],row['x2'],row['y1'],row['y2']),self.__width-1,reso)
            mat = mzd.getRecordsAsMatrix(x1,x2,y1,y2)
            batch[i,:self.__width-1,:self.__width-1,0] = self.preprocess(mat)
          prediction = self.__model.predict(batch)
          df_tmp.loc[:,:]['score_oracle_' + str(reso)] = prediction#.reshape(prediction.shape[0], )
          # scores.append(df_tmp)
        # print ('finished analyzing chromosome', chr, flush=True)
        # self.__oracleList.append(pd.concat(scores,ignore_index = True))
        self.__oracleList.append(df_tmp)
        return f'Finished analyzing {chr}'


    def make_predictions_single_thread(self, chromosome):
        passed, failed = [], []
        for reso, sublist in self.__resolution_sub_lists.items():
            print('ORACLE is running at', reso, 'kb', 'on', chromosome)

            if len(failed) > 0:
                # failed.drop(['prediction'],axis=1,inplace=True)
                failed = failed.loc[:, ~failed.columns.str.contains('^score_oracle_', case=False)]
                sublist = pd.concat([sublist, failed], ignore_index=True)

            sublist = sublist[sublist['chr1'] == chromosome]
            if sublist.shape[0] == 0:
                continue
            sublist = sublist.reset_index(drop=True)
            batch = np.zeros((len(sublist), self.__width, self.__width, 1))

            mzd = self.__hic.getMatrixZoomData(chromosome, chromosome, "observed", self.__norm, "BP", reso)
            for index, row in sublist.iterrows():
                x1, x2, y1, y2 = make_region((row[CHROM_KEY], row[X1_KEY], row[X2_KEY], row[Y1_KEY], row[Y2_KEY]),
                                             self.__width - 1, reso)
                mat = mzd.getRecordsAsMatrix(x1, x2, y1, y2)

                batch[index, :self.__width - 1, :self.__width - 1, 0] = self.preprocess(mat)
            prediction = self.__model.predict(batch)
            sublist['score_oracle_' + str(reso)] = prediction.reshape(prediction.shape[0], )
            psd = sublist[sublist['score_oracle_' + str(reso)] >= 0.5]
            passed.append(psd)
            failed = sublist[sublist['score_oracle_' + str(reso)] < 0.5]
            print(psd.shape[0], 'calls passed ORACLE.')
            print(failed.shape[0], 'calls failed ORACLE.')
            # psd.to_csv(filename + '_ORACLE_passed_'+str(reso)+'.bedpe', sep="\t", index=False)
            # failing.to_csv(filename + '_ORACLE_failed_'+str(reso)+'.bedpe', sep="\t", index=False)

        return pd.concat(passed, ignore_index=True).fillna('.'), failed


    def run(self):
        results = []
        with ThreadPoolExecutor(max_workers = self.__numWorkers) as executor:
          results = [executor.submit(self.makePredictions, x) for x in self.__chr]
          for r in as_completed(results):
            print (r.result())
          print('All Oracle jobs submitted', flush=True)
          df = pd.concat(self.__oracleList,ignore_index=True).fillna('.')
          df.to_csv(self.__outputDir+'/'+self.__stem+'_ORACLE_merged.bedpe', sep = "\t", index=False)


    def run_single_thread(self):
        passed, failed = [], []
        for chrom in self.__chr:
            prediction = self.make_predictions_single_thread(chrom)
            passed.append(prediction[0])
            failed.append(prediction[1])

        return pd.concat(passed, ignore_index=True).fillna('.'), pd.concat(failed, ignore_index=True)


# python3 oracle.py <file.hic> </dir/models> </dir/bedpe> <norm> <num_workers> <stem>

if __name__ == "__main__":
    FILEPATH = sys.argv[1]
    MODEL_DIR = sys.argv[2]
    BEDPE_DIR = sys.argv[3]
    NORMALIZATION_TYPE = sys.argv[4]
    STEM = sys.argv[5]
    NUM_WORKERS = sys.argv[6]
    OUTPUT_DIR = sys.argv[7]
    if len(sys.argv) < 9:
        CHR_LIST = None
    else:
        CHR_LIST = sys.argv[8].split(',')

    oracle = Oracle(BEDPE_DIR, FILEPATH, MODEL_DIR, NORMALIZATION_TYPE, STEM, NUM_WORKERS, OUTPUT_DIR, chr_list=CHR_LIST)
    # passing, failing = oracle.run()
    oracle.run()

    print('Saving results to disk...')

    # filename = BEDPE_DIR.split('/')[-1].replace('.bedpe', "")

    # passing.to_csv(filename + '_ORACLE_passed.bedpe', sep="\t", index=False)
    # failing.to_csv(filename + '_ORACLE_failed.bedpe', sep="\t", index=False)

    print('Done.')

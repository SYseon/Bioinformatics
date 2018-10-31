import pandas as pd
from preprocess import *
from classifier import *
from fselector import *
import numpy as np


class Model:
    def __init__(self):
        self.f_train = None
        self.f_test = None
        self.fea_list = None
        self.nparr_train = None
        self.nparr_test = None

        self.tr_data = None
        self.tr_ans = None
        self.ts_data = None
        self.ts_ans = None

        self.pre_tr_data =None
        self.pre_ts_data = None

        self.preprocessor = Preprocessor()
        self.classifier = Classifier()
        self.fselector = FSelector()

        self.file_set = False

    def set_tr_file(self, file_name):
        self.f_train = pd.read_excel(file_name)  # Excel 파일 열음
        self.fea_list = np.array(self.f_train.columns)
        self.nparr_train = np.array(self.f_train.values)
        self.file_set = False

    def set_ts_file(self, file_name):
        self.f_test = pd.read_excel(file_name)
        self.nparr_test = np.array(self.f_test.values)
        self.file_set = False
        
    def get_nparr_train(self):
        return self.nparr_train

    def set_answer(self, answer_idx):
        self.tr_data = np.delete(self.nparr_train, np.s_[answer_idx:answer_idx+1], axis=1)
        self.tr_ans = self.nparr_train[:, answer_idx].flatten()

        self.ts_data = np.delete(self.nparr_test, np.s_[answer_idx:answer_idx+1], axis=1)
        self.ts_ans = self.nparr_test[:, answer_idx].flatten()
        self.fea_list = np.delete(self.fea_list, np.s_[answer_idx:answer_idx+1])
        self.file_set = False
        

    def get_fea_list(self):
        return np.ndarray.tolist(self.fea_list)

    def remove_var_zero(self):
        var_vec = np.var(self.tr_data, axis=0)
        zero_idx = np.argwhere(var_vec == 0)
        

        self.tr_data = np.delete(self.tr_data, zero_idx, axis=1)
        self.ts_data = np.delete(self.ts_data, zero_idx, axis=1)
        self.fea_list = np.delete(self.fea_list, zero_idx)
        self.file_set = True

    def set_preprocess_data(self, alg_idx):
        self.pre_tr_data, self.pre_ts_data = self.preprocessor.preprocessing(alg_idx, self.tr_data, self.ts_data)

    def start_classify(self, alg_idx):
        return self.classifier.get_result(alg_idx, self.pre_tr_data, self.tr_ans, self.pre_ts_data, self.ts_ans)

    def set_fs_data(self, alg_idx):
        self.pre_tr_data, self.pre_ts_data = self.fselector.start_fs(alg_idx, self.pre_tr_data, self.tr_ans, self.pre_ts_data)

    def set_fs_size(self, fs_size):
        self.fselector.set_fs_size(fs_size)
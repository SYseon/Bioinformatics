# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 03:26:59 2018

@author: 선승엽
"""
from sklearn import preprocessing
from tkinter import simpledialog
import numpy as np

class Preprocessor:
    def __init__(self):
        self.alg_list =  ['None','standard_norm', 'min-max']
        self.preprocessor_name = None
    def preprocessing(self, alg_idx, tr_data, ts_data):
        """
        for i in range(tr_data.shape[1]):
            tr_data.T[i]=np.where(np.isnan(tr_data.T[i]) and tr_data.T[i]==tr_data.T[i].astype(int),np.mean(tr_data.T[i]), tr_data.T[i])
        for j in range(ts_data.shape[1]):
            ts_data.T[i]=np.where(np.isnan(ts_data.T[i]) and ts_data.T[i]==ts_data.T[i].astype(int),np.mean(ts_data.T[i]), ts_data.T[i])
        """
        if alg_idx == 0:
            self.preprocessor_name = self.alg_list[0]
            return tr_data, ts_data
        elif alg_idx == 1:
            
            self.preprocessor_name = self.alg_list[1]
            return self.standard_normalization(tr_data, ts_data)
        elif alg_idx ==2:
            
            self.preprocessor_name = self.alg_list[2]
            return self.min_max(tr_data, ts_data)


    def standard_normalization(self, tr_data, ts_data):
        scaler = preprocessing.StandardScaler().fit(tr_data)
        pre_tr_data = scaler.transform(tr_data)
        pre_ts_data = scaler.transform(ts_data)

        return pre_tr_data, pre_ts_data

    def min_max(self, tr_data, ts_data):
        min_val = simpledialog.askinteger("Input", "최소값을 입력하시오")
        max_val = simpledialog.askinteger("Input", "최대값을 입력하시오")
        scaler = preprocessing.MinMaxScaler(feature_range=(min_val, max_val)).fit(tr_data)

        pre_tr_data = scaler.transform(tr_data)
        pre_ts_data = scaler.transform(ts_data)

        return pre_tr_data, pre_ts_data

    def get_alg_list(self):
        return self.alg_list




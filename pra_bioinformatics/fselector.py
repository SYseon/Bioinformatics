import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mutual_info_score

class FSelector:
    alg_list = None
    fs_size = 0

    def __init__(self):
        self.alg_list = ['PCC', 'PCA', 'filter', 'Wrapper']
        self.fselector_name = None
    def start_fs(self, alg_idx, tr_data, tr_ans, ts_data, ts_ans, calg_idx):
        if alg_idx == 0:
            self.fselector_name = self.alg_list[0]
            return self.pcc(tr_data, tr_ans, ts_data)
        elif alg_idx == 1:
            self.fselector_name = self.alg_list[1]
            return self.pca(tr_data, ts_data)
        elif alg_idx == 2:
            self.fselector_name = self.alg_list[2]
            return self._filter(tr_data, ts_data)
        elif alg_idx == 3:
            self.fselector_name = self.alg_list[3]
            return self.wrapper(tr_data, tr_ans, ts_data, ts_ans, calg_idx)

    def pcc(self, tr_data, tr_ans, ts_data):
        corr_array = []
        for i in range(0, tr_data.shape[1]):
            corr_array.append(np.corrcoef(tr_data[:, i], tr_ans)[0, 1])
        corr_array = np.square(corr_array)
        pcc_feature_idx = np.flip(np.argsort(corr_array), 0)
        fs_tr_data = tr_data[:, pcc_feature_idx[0:self.fs_size]]
        fs_ts_data = ts_data[:, pcc_feature_idx[0:self.fs_size]]

        return fs_tr_data, fs_ts_data

    def pca(self, tr_data, ts_data):
        pca = PCA(n_components=self.fs_size)
        pca.fit(tr_data)

        fs_tr_data = pca.transform(tr_data)
        fs_ts_data = pca.transform(ts_data)

        return fs_tr_data, fs_ts_data

    def _filter(self, tr_data, ts_data):
        fs_tr_data=self.filter_func(tr_data)
        fs_ts_data=self.filter_func(ts_data)
        
        return fs_tr_data, fs_ts_data
    
    def filter_func(self, data):
        index=np.empty(0)
        for i in range (data.shape[1]):
            for j in range (i):
                np.append(index, np.where(mutual_info_score(data.T[i], data.T[j])!=1, j, None))
                
                
        return np.take(data, index)
 

    def wrapper(self, tr_data, tr_ans, ts_data, ts_ans, calg_idx):
        index = np.empty(0)
        classify = classifier.Classifier()
        
        for i in range(tr_data.shape[1]):
            for j in range(tr_data.shape[1]-i):
                np.append(index, j)
                classify.get_result(calg_idx, np.take(tr_data.T, index), tr_ans, ts_data, ts_ans)
    
                

    
        
        
    def set_fs_size(self, fs_size):
        self.fs_size = fs_size

    def get_alg_list(self):
        return self.alg_list







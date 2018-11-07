# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:10:55 2018

@author: 선승엽
"""

import numpy as np


def data_type_indicator(data):  # 데이터 타입을 배열로 반환
    temp = list()

    for i in range(data.shape[1]):
        # string data
        if np.any(data.T[i] == data.T[i].astype(str)):
            temp.append(2)

        # categorical data
        elif len(np.unique(data.T[i].astype(float))) < 7:
            temp.append(0)

        # continuous data
        elif np.any(data.T[i].astype(int) != data.T):
            temp.append(1)

    result = np.array(temp)
    result = np.unique(result)

    if len(result) == 1:
        return result[0]
    else:
        return 3



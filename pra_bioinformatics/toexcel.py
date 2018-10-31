# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:14:03 2018

@author: leedongjae
"""

# import modules
import pandas as pd
import numpy as np
 
idx = 1
def excel_init():    

    # index_format(index) & columns_format(columns)정의
    columns_format = ['전처리기 타입', '특징 선택 타입' ,'분류기 타입', '결과값']
    # DataFrame 초기화
    values = pd.DataFrame(columns=columns_format)
    # saves DataFrame(values) into an Excel file
    values.to_excel('./test.xlsx',
        sheet_name='Sheet1',
        columns=columns_format,
        header=True,
        startrow=1,
        startcol=0,
        engine=None,
        merge_cells=True,
        encoding=None,
        inf_rep='inf',
        verbose=True,
        freeze_panes=None
    )

def set_value(preprocessor_name, fselector_name, classifier_name, result_value):
    global idx
    excel_filename = './test.xlsx'
    wb = load_workbook(filename = excel_filename)
    # get the worksheet
    ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])
    
    ws.cell(row=idx, column=1).value = preprocessor_name
    ws.cell(row=idx, column=2).value = fselector_name
    ws.cell(row=idx, column=3).value = classifier_name
    ws.cell(row=idx, column=4).value = result_value
    
    idx+=1
    
    wb.save(filename='./test.xlsx')

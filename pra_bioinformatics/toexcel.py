# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:14:03 2018

@author: leedongjae
"""

# import modules
import pandas as pd
import numpy as np
from openpyxl import load_workbook 
 
idx = 1
def excel_init():    

    # index_format(index) & columns_format(columns)정의
    columns_format = ['전처리기', '특징 선택' ,'분류기', 'Accuracy', 'Precision 1', 'Precision 2', 'Recall 1', 'Recall 2', 'fbeta score 1', 'fbeta score 2', 'Support 1', 'Support 2']
    # DataFrame 초기화
    values = pd.DataFrame(columns=columns_format)
    # saves DataFrame(values) into an Excel file
    values.to_excel('./test.xlsx',
        sheet_name='Sheet1',
        columns=columns_format,
        header=True,
        startrow=0,
        startcol=0,
        engine=None,
        merge_cells=True,
        encoding=None,
        inf_rep='inf',
        verbose=True,
        freeze_panes=None
    )

def set_value(file_name, preprocessor_name, fselector_name, classifier_name, result_value, precision, recall, fbeta_score, support):
    global idx
    excel_filename = './test.xlsx'
    wb = load_workbook(filename = excel_filename)
    
    
    # get the worksheet
  
    ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])
    ws.cell(row=1, column=1).value = file_name.split('/')[-1]
    ws.cell(row=idx+1, column=2).value = preprocessor_name
    ws.cell(row=idx+1, column=3).value = fselector_name
    ws.cell(row=idx+1, column=4).value = classifier_name
    ws.cell(row=idx+1, column=5).value = result_value
    ws.cell(row=idx+1, column=6).value = precision[0]
    ws.cell(row=idx+1, column=7).value = precision[1]
    ws.cell(row=idx+1, column=8).value = recall[0]
    ws.cell(row=idx+1, column=9).value = recall[1]
    ws.cell(row=idx+1, column=10).value = fbeta_score[0]
    ws.cell(row=idx+1, column=11).value = fbeta_score[1]
    ws.cell(row=idx+1, column=12).value = support[0]
    ws.cell(row=idx+1, column=13).value = support[1]
    
    idx+=1
    
    wb.save(filename='./test.xlsx')

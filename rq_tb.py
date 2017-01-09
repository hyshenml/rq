# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
import pandas as pd
import numpy as np
import re
import time
import datetime

def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook(r'e:/data/rq.xlsx')
  # 获取所有sheet

  sheet2 = workbook.sheet_by_name(u'明细表')
 
  # sheet的名称，行数，列数
 
  # 获取整行和整列的值（数组）
  rows = sheet2.row_values(3) # 获取第四行内容
  cols = sheet2.col_values(2) # 获取第三列内容
 
  # 获取单元格内容
  print sheet2.cell(1,0).value.encode('utf-8')
  print sheet2.cell_value(1,0).encode('utf-8')
  print sheet2.row(1)[0].value.encode('utf-8')
  return sheet2
   
sheet=read_excel()
#%%
title=sheet.row_values(0)
shape=[sheet.nrows,sheet.ncols]
data=[]
for i in range(2,shape[0]):
    data.append(sheet.row_values(i))
data=np.array(data)
data=pd.DataFrame(data)
#%%
col_id={}
for i in range(len(title)):
    if title[i]!='':
        col_id[i]=title[i]
data=data[[id for id in col_id]]
data.columns=[col_id[id] for id in col_id]
#%%
def find_last_update(l):
    if l is not None and len(l)!=0:
        
        for d in l:
            if len(d[0])==4:
                year=int(d[0])
            else:
                year=2016
            month=int(d[1])
            day=int(d[2])
            if 0<month<13 and 0<day<32:
                return datetime.date(year,month,day)
    return None
     

p=re.compile(r'(\d{4})?.(\d{1,2}).(\d{1,2})')
comments=data[u'备注']
update_time=[]
for line in comments:
    date_line=re.findall(p,line)
    update_time.append(find_last_update(date_line))
data['update']=update_time
    
#%%
check_day=datetime.date(2016,12,17)
today=datetime.date(2016,12,21)
  
def get_key(d,value):
    try:
        return [k for k in d if d[k]==value][0]
    except Exception,e:
        return None
#%%
d2=data
d2=d2.ix[d2[u'实际状态']!=u'需求完成']
d2=d2.ix[d2[u'实际状态']!=u'暂停']
d2=d2.ix[d2[u'实际状态']!=u'停止']
d2=d2.ix[(d2['update']<check_day)|(d2['update']>today)|(d2['update'].isnull())]  

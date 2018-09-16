# coding:utf-8

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('day.csv')
print(data.shape)
cols=cat.columns
for col in cols:
    print("%s 出现的类别型特征进行统计出现的次数是：",col)
    print(data[col].value_counts())

y_data=data['cnt']
figure=plt.figure()
from sklearn.model_selection import GridSearchCV
bins=[10,20,30,40]
i=1
for bin in bins:
    ax=figure.add_subplot(int('22'+str(i)))
    sns.distplot(y_data,bins=bin,kde=True)
    i+=1


plt.subplots(figsize=(20,15))
cols=data.columns
data_corr=data.corr().abs()
sns.heatmap(data_corr,annot=True)
plt.show()
list_1=[]
for i in range(0,data_corr.shape[0]):
    for j in range(i+1,data_corr.shape[0]):
        if data_corr.iloc[i,j]>0.5:
            list_1.append([i,j,data_corr.iloc[i,j]])
list_1=sorted(list_1,key=lambda x:x[2],reverse=True)
for i,j,v in list_1:
    print('%s and %s 的相关系数是：%s'%(cols[i],cols[j],data_corr.iloc[i,j]))
        

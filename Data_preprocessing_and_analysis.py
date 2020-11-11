#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('./hotel_bookings_dataset.csv')
data.head()

data['hotel'].value_counts()
len(data)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))
data.head()

import numpy as np
data = data.replace('NULL',np.NaN)
print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))
print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))

data = data.drop(['company'],axis=1)
data.head()

data = data.replace(np.NaN,'0')
data.head()
data.dtypes

get_ipython().run_line_magic('matplotlib', 'inline')
data.boxplot(figsize=(150,50))

data.describe()

dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))
data.loc[[11,28]]

data.cov()

data.corr()

plt.figure(figsize=(8,2))
data.corr()['is_canceled'].sort_values()[:-1].plot(kind='bar')
plt.show()

plt.style.use('fivethirtyeight')
plt.figure(figsize=(14,6))
sns.countplot(x='hotel',data=data,hue='is_canceled',palette='pastel')
plt.show()

data['arrival_date'] = data['arrival_date_year'].astype(str)+'-' + data['arrival_date_month'] + '-' + data['arrival_date_day_of_month'].astype(str)
data['arrival_date'] = data['arrival_date'].apply(pd.to_datetime)
data['reservation_status_date'] = data['reservation_status_date'].apply(pd.to_datetime)

cancelled_data = data[data['reservation_status'] == 'Canceled']
cancelled_data['canc_to_arrival_days'] = cancelled_data['arrival_date'] - cancelled_data['reservation_status_date']
cancelled_data['canc_to_arrival_days'] = cancelled_data['canc_to_arrival_days'].dt.days


plt.figure(figsize=(14,6))
sns.distplot(cancelled_data['canc_to_arrival_days'])
plt.show()

print('Percentage of cancellations that are within a week of arrival: ', 
      (cancelled_data[cancelled_data['canc_to_arrival_days']<=7]['canc_to_arrival_days'].count()*100/cancelled_data['canc_to_arrival_days'].count()).round(2), '%')


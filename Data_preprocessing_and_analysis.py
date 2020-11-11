#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/Users/ashutoshshanker/Desktop/Dataset_BI_Project/hotel_bookings_dataset.csv')

data.head()


# In[2]:


data['hotel'].value_counts()


# In[3]:


len(data)


# In[4]:


print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))
data.head()


# In[5]:


import numpy as np

data = data.replace('NULL',np.NaN)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))


# In[6]:


data = data.drop(['company'],axis=1)


# In[7]:


data.head()


# In[8]:


import numpy as np
data = data.replace(np.NaN,'0')


# In[9]:


data.head()


# In[10]:


data.dtypes


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')

data.boxplot(figsize=(150,50))


# In[12]:


data.describe()


# In[13]:


dups = data.duplicated()
print('Number of duplicate rows = %d' % (dups.sum()))
data.loc[[11,28]]


# In[14]:


data.cov()


# In[15]:


data.corr()


# In[16]:


plt.figure(figsize=(8,2))
data.corr()['is_canceled'].sort_values()[:-1].plot(kind='bar')
plt.show()


# In[17]:


import pandas as pd

data = pd.read_csv('/Users/ashutoshshanker/Desktop/Dataset_BI_Project/clean_data_hotel_1.csv')

data.head()


# In[18]:


data['hotel'].value_counts()


# In[19]:


len(data)


# In[20]:


print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))
data.head()


# In[21]:


import numpy as np

data = data.replace('NULL',np.NaN)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))


# In[22]:


import numpy as np
data = data.replace(np.NaN,'0')
data.head()


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')

data.boxplot(figsize=(150,50))


# In[24]:


plt.style.use('fivethirtyeight')


# In[25]:


plt.figure(figsize=(14,6))
sns.countplot(x='hotel',data=data,hue='is_canceled',palette='pastel')
plt.show()


# In[26]:


data['arrival_date'] = data['arrival_date_year'].astype(str)+'-' + data['arrival_date_month'] + '-' + data['arrival_date_day_of_month'].astype(str)
data['arrival_date'] = data['arrival_date'].apply(pd.to_datetime)
data['reservation_status_date'] = data['reservation_status_date'].apply(pd.to_datetime)


# In[27]:


cancelled_data = data[data['reservation_status'] == 'Canceled']
cancelled_data['canc_to_arrival_days'] = cancelled_data['arrival_date'] - cancelled_data['reservation_status_date']
cancelled_data['canc_to_arrival_days'] = cancelled_data['canc_to_arrival_days'].dt.days


# In[28]:


plt.figure(figsize=(14,6))
sns.distplot(cancelled_data['canc_to_arrival_days'])
plt.show()


# In[29]:


print('Percentage of cancellations that are within a week of arrival: ', 
      (cancelled_data[cancelled_data['canc_to_arrival_days']<=7]['canc_to_arrival_days'].count()*100/cancelled_data['canc_to_arrival_days'].count()).round(2), '%')


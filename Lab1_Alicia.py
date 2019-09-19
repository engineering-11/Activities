#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[9]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv?mwwbbozji')


# In[10]:


data


# In[11]:


data.describe()


# In[6]:


cpm_data = data.loc[:,'deviceTime_local':'cpmError']
cpm_data = data.drop(['deviceTime_utc','deviceTime_unix'],axis=1)
cpm_data


# In[12]:


print(cpm_data.max())
print(cpm_data.min())


# In[13]:


cpm_data.loc[:,'cpm']>0
mask = cpm_data.loc[:,'cpm']>0
print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data


# In[14]:


time_mask = good_cpm_data['deviceTime_local'] > '2019-08-05 00:00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[15]:


plt.plot(good_cpm_data['cpm'])
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[16]:


plt.hist(month_cpm['cpm'],bins=31)
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[18]:


np.mean(good_cpm_data['cpm'])


# In[20]:


np.std(good_cpm_data['cpm'])


# In[21]:


np.mean(month_cpm['cpm'])


# In[22]:


np.std(month_cpm['cpm'])


# In[23]:


data=pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv')
data


# In[24]:


data.describe()


# In[25]:


cpm_data2 = data.loc[:,'deviceTime_local':'cpmError']
cpm_data2 = data.drop(['deviceTime_utc','deviceTime_unix'],axis=1)
cpm_data2


# In[28]:


print(cpm_data.max())
print(cpm_data.min())


# In[29]:


cpm_data2.loc[:,'cpm']>0
mask = cpm_data2.loc[:,'cpm']>0
print(mask)
good_cpm_data2 = cpm_data2[mask]
good_cpm_data2


# In[30]:


time_mask2 = good_cpm_data2 ['deviceTime_local'] > '2019-08-05 00:00:00:00-07:00'
#print(time_mask2)
month_cpm2 = good_cpm_data2 [time_mask2]
month_cpm2


# In[31]:


plt.plot(good_cpm_data2['cpm'])
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[32]:


plt.hist(month_cpm2['cpm'], bins = 31)
plt.ylabel('frequency')
plt.xlabel('Counts per Minute')
plt.show()


# In[33]:


plt.hist(month_cpm2['cpm'], bins = 31)
plt.hist(month_cpm['cpm'],bins = 31)
plt.ylabel('frequency')
plt.xlabel('Counts per Minute')
plt.show()


# In[37]:


np.mean(good_cpm_data2['cpm'])


# In[38]:


np.std(good_cpm_data2['cpm'])


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[3]:


data


# In[4]:


data.describe()


# In[5]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis = 1)
cpm_data


# In[6]:


print(cpm_data.max())
print(cpm_data.min())


# In[7]:


cpm_data.loc[:,"cpm"] > 0.0
mask = cpm_data["cpm"] > 0.0
#print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[8]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm= good_cpm_data[time_mask]
month_cpm


# In[9]:


plt.plot(good_cpm_data ["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("CPM vs index")
plt.show()


# In[10]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[11]:


print(cpm_data['cpm'].mean())


# In[12]:


data2 = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?ywkqgtfgc')


# In[13]:


data2


# In[14]:


data2.describe()


# In[15]:


cpm_data2 = data2.loc[:,"deviceTime_local":"cpmError"]
cpm_data2 = cpm_data2.drop(["deviceTime_unix"],axis = 1)
cpm_data2


# In[16]:


print(cpm_data2.max())
print(cpm_data2.min())


# In[17]:


cpm_data.loc[:,'cpm'] > 0.0
mask2 = cpm_data2['cpm'] > 0.0
good_cpm_data2 = cpm_data2[mask2]
good_cpm_data2.min()


# In[18]:


time_mask2 = good_cpm_data2['deviceTime_local'] > '2019-08-05 00:00:00-07:00'
month_cpm2 = good_cpm_data2[time_mask2]
month_cpm2


# In[19]:


plt.plot(good_cpm_data2['cpm'])
plt.ylabel('Counts per Minute')
plt.title("CPM vs Index")
plt.show


# In[20]:


plt.hist(month_cpm2["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[21]:


print(cpm_data2['cpm'].mean())


# In[23]:


plt.hist(month_cpm['cpm'],bins=31, label='Etch Roof CPM')
plt.hist(month_cpm2['cpm'],bins=31, label = 'Nora Real Gym')
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.legend()
plt.show()


# In[ ]:





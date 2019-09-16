#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[3]:


data


# In[4]:


data.describe()


# In[5]:


cpm_data=data.loc[:,"deviceTime_local":"cpmError"]
cpm_data=cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[6]:


cpm_data.loc[:,"cpm"]>0.0
mask=cpm_data["cpm"]>0.0
good_cpm_data=cpm_data[mask]
good_cpm_data.min()


# In[7]:


time_mask=good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm=good_cpm_data[time_mask]
month_cpm


# In[8]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("CPM vs index")
plt.show()


# In[9]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[10]:


print(cpm_data.max())
print(cpm_data.min())


# In[11]:


np.mean(good_cpm_data["cpm"])


# In[12]:


np.std(good_cpm_data["cpm"])


# In[13]:


data_norra=pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?eqcanxbhf')


# In[14]:


cpm_data_norra=data_norra.loc[:,"deviceTime_local":"cpmError"]
cpm_data_norra=cpm_data_norra.drop(["deviceTime_unix"],axis=1)


# In[15]:



cpm_data_norra.loc[:,"cpm"] > 0.0
mask = cpm_data_norra["cpm"] > 0.0
good_cpm_data_norra = cpm_data_norra[mask]
good_cpm_data_norra.min()


# In[16]:


time_mask = good_cpm_data_norra['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm_norra = good_cpm_data_norra[time_mask]


# In[17]:


plt.plot(good_cpm_data_norra["cpm"])
plt.ylabel('Counts Per Minute')                       
plt.title("CPM vs index")                               
plt.show()


# In[ ]:





# In[18]:


plt.plot(good_cpm_data["cpm"])
plt.plot(good_cpm_data_norra["cpm"])
plt.ylabel('Counts Per Minute')                       
plt.title("CPM vs index")                               
plt.show()


# In[19]:


np.mean(good_cpm_data_norra["cpm"])


# In[20]:


np.std(good_cpm_data_norra["cpm"])


# In[21]:


plt.hist(month_cpm["cpm"],bins=31)
plt.hist(month_cpm_norra["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[29]:


plt.hist(month_cpm_norra["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[ ]:





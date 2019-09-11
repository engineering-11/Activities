#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv?ipcoms')


# In[5]:


data


# In[6]:


data.describe()


# In[7]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[8]:


print(cpm_data.max())
print(cpm_data.min())


# In[9]:


mask = cpm_data["cpm"]>0.0
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[10]:


time_mask = good_cpm_data["deviceTime_local"]>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[11]:


plt.plot(good_cpm_data["cpm"])
plt.xlabel('Index')
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[12]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel("Frequency")
plt.xlabel("Counts per Minute")
plt.show()


# In[13]:


np.mean(good_cpm_data.cpm)


# In[14]:


np.std(good_cpm_data.cpm)


# In[15]:


data_new = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?dodiq')


# In[16]:


data_new


# In[17]:


data_new.describe()


# In[18]:


cpm_data_new = data_new.loc[:,"deviceTime_local":"cpmError"]
cpm_data_new = cpm_data_new.drop(["deviceTime_unix"],axis=1)
cpm_data_new


# In[19]:


print(cpm_data_new.max())
print(cpm_data_new.min())


# In[20]:


mask_new = cpm_data_new["cpm"]>0.0
good_cpm_data_new = cpm_data_new[mask_new]
good_cpm_data_new.min()


# In[21]:


time_mask_new = good_cpm_data_new["deviceTime_local"]>'2016-12-29 21:07:58+01:00'
month_cpm_new = good_cpm_data_new[time_mask_new]
month_cpm_new


# In[27]:


plt.plot(good_cpm_data_new["cpm"], color = 'green')
plt.xlabel('Index')
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[28]:


plt.hist(month_cpm_new["cpm"],bins=60, color = 'green')
plt.ylabel("Frequency")
plt.xlabel("Counts per Minute")
plt.show()


# In[24]:


np.mean(good_cpm_data_new.cpm)


# In[25]:


np.std(good_cpm_data_new.cpm)


# In[29]:


plt.plot(good_cpm_data["cpm"])
plt.xlabel('Index')
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()
plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel("Frequency")
plt.xlabel("Counts per Minute")
plt.show()
plt.plot(good_cpm_data_new["cpm"], color='green')
plt.xlabel('Index')
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()
plt.hist(month_cpm_new["cpm"],bins=60, color = 'green')
plt.ylabel("Frequency")
plt.xlabel("Counts per Minute")
plt.show()


# In[ ]:





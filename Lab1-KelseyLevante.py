#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[11]:


data


# In[12]:


data.describe


# In[13]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[14]:


cpm_data.loc[:,"cpm"] > 0.0
mask = cpm_data["cpm"] > 0.0
print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


time_mask = good_cpm_data['deviceTime_local'] > '2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[16]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')
a = "Title"
plt.title(a)
plt.show()


# In[17]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[18]:


np.mean(good_cpm_data["cpm"])


# In[19]:


np.std(good_cpm_data["cpm"])


# In[24]:


data1 = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/campolindo.csv')


# In[21]:


data1


# In[25]:


data1.describe()


# In[26]:


cpm_data1 = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data1 = cpm_data1.drop(["deviceTime_unix"],axis=1)
cpm_data1


# In[27]:


cpm_data1.loc[:,"cpm"] > 0.0
mask = cpm_data1["cpm"] > 0.0
print(mask)
good_cpm_data1 = cpm_data1[mask]
good_cpm_data1.min()


# In[ ]:


time_mask = good_cpm_data1['deviceTime_local'] > '2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data1[time_mask]
month_cpm


# In[ ]:


plt.plot(good_cpm_data1["cpm"])
plt.ylabel('Counts Per Minute')
a = "Title"
plt.title(a)
plt.show()


# In[ ]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[ ]:


np.mean(good_cpm_data["cpm"])


# In[ ]:


np.std(good_cpm_data["cpm"])


# In[ ]:





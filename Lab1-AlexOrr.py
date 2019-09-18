#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# This line allows plots to show in the Jupyter notebook
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[3]:


data


# In[4]:


data.describe()


# In[10]:


cpm_data=data.loc[:,"deviceTime_local":"cpmError"]
cpm_data


# In[11]:


cpm_data=cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[12]:


print(cpm_data.max())
print(cpm_data.min())


# In[13]:


cpm_data.loc[:,"cpm"]>0.0
mask=cpm_data["cpm"]>0.0
good_cpm_data=cpm_data[mask]
good_cpm_data.min()


# In[14]:


print(mask)


# In[15]:


time_mask=good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-7:00'
month_cpm=good_cpm_data[time_mask]
month_cpm


# In[16]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[18]:


plt.hist(month_cpm['cpm'],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.title('Frequency vs CPM')
plt.show


# In[22]:


cpm_mean=np.mean(month_cpm["cpm"])
print(cpm_mean)


# In[25]:


cpm_stddev=np.std(month_cpm["cpm"])
print(cpm_stddev)


# In[35]:


data2=pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv')                


# In[36]:


data2


# In[37]:


data2.describe()


# In[38]:


cpm_data2=data2.loc[:,"deviceTime_local":"cpmError"]
cpm_data2


# In[39]:


cpm_data2=cpm_data2.drop(["deviceTime_unix"],axis=1)
cpm_data2


# In[40]:


print(cpm_data2.max())
print(cpm_data2.min())


# In[41]:


cpm_data2.loc[:,"cpm"]>0.0
mask2=cpm_data2["cpm"]>0.0
good_cpm_data2=cpm_data2[mask2]
good_cpm_data2.min()


# In[43]:


time_mask2 = good_cpm_data2['deviceTime_local']>'2019-08-05 00:00:00-02:00'
month_cpm2 = good_cpm_data2[time_mask2]
month_cpm2


# In[44]:



plt.plot(good_cpm_data2["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("CPM vs index at Nora Real Gymnasium")
plt.show()


# In[45]:


plt.hist(month_cpm2["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.title('Frequency vs CPM at Nora Real Gymnasium')
plt.show()


# In[46]:


cpm_mean2=np.mean(month_cpm2["cpm"])
print(cpm_mean2)


# In[47]:


cpm_stddev2=np.std(month_cpm2["cpm"])
print(cpm_stddev2)


# In[51]:


plt.plot(good_cpm_data["cpm"], label='Etchevery Roof')
plt.plot(good_cpm_data2["cpm"], label='Nora Real Gymnasium')
plt.xlabel('Index')
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index for Both Locations')
plt.legend(loc='upper right')
plt.show()


# In[52]:


plt.hist(good_cpm_data["cpm"], label='Etchevery Roof')
plt.hist(good_cpm_data2["cpm"], label='Nora Real Gymnasium')
plt.xlabel('Counts Per Minute')
plt.ylabel('Frequency')
plt.title('Frequency vs CPM for Both Locations')
plt.legend(loc='upper right')
plt.show()


# In[ ]:





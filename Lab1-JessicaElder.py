#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[5]:


data


# In[6]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[7]:


print(cpm_data.max())
print(cpm_data.min())


# In[8]:


cpm_data.loc[:,"cpm"] > 0.0
mask = cpm_data["cpm"] > 0.0
#print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[9]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[10]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')                       
plt.title("CPM vs index")                                  
plt.show()


# In[11]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[12]:


good_cpm_data.describe()


# In[13]:


data2 = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?fkghmwkrm')


# In[14]:


data2


# In[15]:


data2.describe()


# In[16]:


cpm_data2 = data2.loc[:, "deviceTime_local" : "cpmError"]


# In[17]:


cpm_data2 = cpm_data2.drop(["deviceTime_unix"], axis=1)


# In[18]:


cpm_data2


# In[19]:


print(cpm_data.max())


# In[20]:


print(cpm_data2.max())
print(cpm_data2.min())


# In[21]:


print(cpm_data.min())


# In[22]:


time_mask2 = cpm_data2['deviceTime_local'] > '2019-08-05 00:00:00-07:00'
month_cpm2 = cpm_data2[time_mask2]
month_cpm2


# In[23]:


plt.plot(cpm_data2["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("Cpm vs Index")
plt.show()


# In[24]:


plt.hist(month_cpm2["cpm"], bins=31)
plt.ylabel("Freq")
plt.xlabel("Counts Per Min")


# In[25]:


cpm_data2.describe()


# In[ ]:





# In[27]:


month_cpm


# In[28]:


month_cpm[0:10]


# In[30]:


month_cpm["cpm"][0:3]


# In[31]:


plt.plot(good_cpm_data["cpm"][0:210000], cpm_data2["cpm"][0:210000])
plt.ylabel("Counts per Minute")
plt.title("CPM vs Index")
plt.show()


# In[32]:


plt.plot(y = [good_cpm_data["cpm"], cpm_data2["cpm"]][0:210000])
plt.ylabel("Counts per Minute")
plt.title("CPM vs Index")
plt.show()


# In[33]:


plt.plot(good_cpm_data["cpm"][0:210000])
plt.plot(cpm_data2["cpm"](0:210000))
plt.ylabel("Counts per Minute")
plt.title("CPM vs Index")
plt.show()


# In[34]:


plt.plot(good_cpm_data["cpm"])
plt.plot(cpm_data2["cpm"])
plt.ylabel('Counts Per Minute')                  
plt.title("CPM vs index")                                 
plt.show()


# In[35]:


plt.hist(month_cpm["cpm"], bins=31)
plt.hist(month_cpm2["cpm"], bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[36]:


plt.hist(month_cpm["cpm"], bins=31)
plt.hist(month_cpm2["cpm"], bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.title("Counts Per Minute of Etcheverry Roof and Somewhere in Switzerland")
plt.show()


# In[ ]:





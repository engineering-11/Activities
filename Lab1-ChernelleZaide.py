#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[13]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[18]:


data


# In[15]:


data.describe()


# In[22]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"], axis=1)
cpm_data


# In[23]:


print(cpm_data.max())
print(cpm_data.min())


# In[25]:


cpm_data.loc[:,"cpm"] > 0.0
mask = cpm_data["cpm"] > 0.0
#print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[26]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]


# In[31]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("CPM vs Time")
plt.show()


# In[33]:


plt.hist(month_cpm["cpm"], bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[34]:


np.mean(month_cpm["cpm"])


# In[35]:


np.std(month_cpm["cpm"])


# In[37]:


norareal = pd.read_csv("https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv")


# In[38]:


norareal


# In[39]:


norareal.describe()


# In[40]:


cpm_norareal = norareal.loc[:,"deviceTime_local":"cpmError"]
cpm_norareal = cpm_norareal.drop(["deviceTime_unix"], axis=1)
cpm_norareal


# In[41]:


print(cpm_norareal.max())
print(cpm_norareal.min())


# In[42]:


cpm_norareal.loc[:,"cpm"] > 0.0
mask = cpm_norareal["cpm"] > 0.0
good_cpm_norareal = cpm_norareal[mask]
good_cpm_norareal.min()


# In[43]:


time_mask = good_cpm_norareal['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_norareal[time_mask]


# In[44]:


plt.plot(good_cpm_norareal["cpm"])
plt.ylabel('Counts Per Minute')
plt.title("CPM vs Time")
plt.show()


# In[45]:


plt.hist(month_cpm["cpm"], bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[46]:


np.mean(month_cpm["cpm"])


# In[47]:


np.std(month_cpm["cpm"])


# In[49]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
time_mask = good_cpm_norareal['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_norareal[time_mask]


# In[74]:


import matplotlib.patches as mpatches
plt.plot(good_cpm_norareal["cpm"])
plt.plot(good_cpm_data["cpm"])
plt.plot(label="Ethecverry Roof")
plt.plot(label="Nora Real")
# line, = ax.plot([1, 2, 3], label='Inline label')
# ax.legend()
plt.ylabel('Counts Per Minute')
plt.title("CPM vs Time")
# plt.legend(loc='upper right')
blue_patch = mpatches.Patch(color='blue', label='Nora Real')
orange_patch = mpatches.Patch(color='orange', label='Etch. Roof')
plt.legend(handles=[blue_patch, orange_patch])
plt.show()


# In[2]:





# In[ ]:


plt.hist(month_cpm["cpm"], bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


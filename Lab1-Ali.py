#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[ ]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv')


# In[ ]:


data


# In[ ]:


data.describe()


# In[ ]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis=1)
cpm_data


# In[ ]:


print(cpm_data.max())
print(cpm_data.min())


# In[ ]:


cpm_data.loc[:,"cpm"] > 0.0
mask = cpm_data["cpm"] > 0.0
#print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[ ]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[ ]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')                       # label the y-axis
plt.title("CPM vs index")                                  # put a title!
plt.show()


# In[ ]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[ ]:


cpm_array = month_cpm["cpm"]
mean = np.mean(cpm_array)
std = np.std(cpm_array)
print("<cpm> = {} +/- {}".format(mean,std))


# In[ ]:





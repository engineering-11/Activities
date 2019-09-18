#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
#get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt



# In[ ]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv?uhekkvtdd')


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


cpm_data.loc[:,"cpm"]>0.0
mask = cpm_data["cpm"]>0.0
print(mask)
good_cpm_data = cpm_data[mask]
good_cpm_data.min()


# In[ ]:


time_mask = good_cpm_data['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm = good_cpm_data[time_mask]
print(month_cpm)


# In[ ]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[ ]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[ ]:


print(np.mean(cpm_data))
print(np.std(cpm_data))
data.mean("cpm")
data.std("cpm")


# In[ ]:





# In[ ]:


dataNOR = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?bxycicyuzh')


# In[ ]:


dataNOR.describe()


# In[ ]:


cpm_dataNOR = dataNOR.loc[:,"deviceTime_local":"cpmError"]
cpm_dataNOR = cpm_dataNOR.drop(["deviceTime_unix"],axis=1)
cpm_dataNOR


# In[ ]:


print(cpm_dataNOR.max())
print(cpm_dataNOR.min())


# In[ ]:


cpm_dataNOR.loc[:,"cpm"]>0.0
mask = cpm_dataNOR["cpm"]>0.0
print(mask)
good_cpm_dataNOR = cpm_dataNOR[mask]
good_cpm_dataNOR.min()


# In[ ]:


time_maskNOR = good_cpm_dataNOR['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpmNOR = good_cpm_dataNOR[time_mask]
print(month_cpmNOR)


# In[ ]:


plt.plot(good_cpm_dataNOR["cpm"])
plt.ylabel('Counts Per Minute')
plt.title('CPM vs Index')
plt.show()


# In[ ]:


plt.hist(month_cpmNOR["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[ ]:


print(np.mean(cpm_dataNOR))
print(np.std(cpm_dataNOR))
dataNOR.mean("cpm")
dataNOR.std("cpm")


# In[7]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots()

fig.add_trace(
    go.Scatter(good_cpm_data["cpm"], name="Etch Roof")

fig.add_trace(
    go.Scatter(good_cpm_dataNOR["cpm"], name="Norra Real")
    
fig.update_layout(title_text="Etch Roof VS Norra Real")

fig.update_xaxes(title_text="Frequency")

fig.update_yaxes(title_text="<b>primary</b> Counts per Minute")

fig.show()


# In[ ]:





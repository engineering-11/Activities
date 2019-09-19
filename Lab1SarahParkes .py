#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 


# In[2]:


data = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/etch_roof.csv?ijfczen')


# In[3]:


data


# In[4]:


data.describe()


# In[5]:


cpm_data = data.loc[:,"deviceTime_local":"cpmError"]
cpm_data = cpm_data.drop(["deviceTime_unix"],axis=1)
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
month_cpm = good_cpm_data[time_mask]
month_cpm


# In[9]:


plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')                       # label the y-axis
plt.title("CPM vs index")                                  # put a title!
plt.show()


# In[10]:


plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.show()


# In[11]:


#What is the mean CPM? What about the standard deviation?
cpm_mean = np.mean(month_cpm)
print ('the cpm mean is ') 
print (cpm_mean) #first value printed is CPM mean for month data 
cpm_standev = np.std(month_cpm)
print ('the cpm standard deviation is ')
print (cpm_standev) #first value printed is CPM standard deviation for month data 


# In[12]:


#Do everything we just did for another location where we have data
data2 = pd.read_csv('https://radwatch.berkeley.edu/sites/default/files/dosenet/norrareal.csv?sluugcam')


# In[13]:


cpm_data2 = data2.loc[:,"deviceTime_local":"cpmError"]
cpm_data2 = cpm_data2.drop(["deviceTime_unix"],axis=1)


# In[14]:


cpm_data2.loc[:,"cpm"] > 0.0
mask2 = cpm_data2["cpm"] > 0.0
good_cpm_data2 = cpm_data2[mask2]


# In[15]:


time_mask2 = good_cpm_data2['deviceTime_local']>'2019-08-05 00:00:00-07:00'
month_cpm2 = good_cpm_data2[time_mask2]


# In[16]:


#find mean and std
cpm_mean2 = np.mean(month_cpm2)
print ("Here's the mean: ")
print (cpm_mean2)
cpm_sdv2 = np.std(month_cpm2)
print ("Here's the standard deviation:")
print (cpm_sdv2)


# In[17]:


#Plot data from these two locations together, including labels
#first, etcheverry histogram 
plt.hist(month_cpm["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.title('Etcheverry Roof Data: CPM v Frequency')
plt.show()
#etcheverry line graph 
plt.plot(good_cpm_data["cpm"])
plt.ylabel('Counts Per Minute')                       # label the y-axis
plt.title("Etcheverry Roof Data: CPM v Index")                                  # put a title!
plt.show()
#Nora Real histogram
plt.hist(month_cpm2["cpm"],bins=31)
plt.ylabel('Frequency')
plt.xlabel('Counts Per Minute')
plt.title('Nora Real Gymnasium Data: CPM v Frequency')
plt.show()
#Nora Real line graph 
plt.plot(good_cpm_data2["cpm"])
plt.ylabel('Counts Per Minute')                       # label the y-axis
plt.title("Noral Real Gymnasium Data: CPM v Index")                                  # put a title!
plt.show()


# In[ ]:


#Extra credit: Make these same plots (line graph, histogram, two locations) using plotly
#note: having trouble importing plotly 


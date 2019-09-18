#!/usr/bin/env python
# coding: utf-8

# # 1. How radioactive are humans?
# 
# ### 1.a. Assume an average human mass of 70kg. What is the activity (Bq) of that person?
#   * Hints:
#     * What elements(isotopes) in our body produce radiation that actually escapes our body?
#     * How much of our body is made up of those elements?
#       * Don’t forget to consider the natural abundance of the unstable isotopes
#     * How much activity will that lead to?
#       * Don’t forget about branching ratios
# 
# ### 1.b. How radioactive are you?
#   * Hint: make use of specific activity
#   * You don’t have to use your actual mass
# 
# ### 1.c. Provide references
#   * Where did you get the relevant numers that went in to your calculations?
#   * Include your references in Markdown

# # 2. What is the activity from a 120g (medium size) banana?
# * Neglect the impact of the banana peel in your answers - assume a uniform composition and assume you will injest the entire banana.
# * Composition of bananas:
#   * Potassium (K)
#   * Vitamin B6 (C<sub>8</sub>H<sub>11</sub>NO<sub>3</sub>)
#   * Vitamin C (C<sub>6</sub>H<sub>8</sub>O<sub>6</sub>)
#   * Isoamyl acetate (C<sub>7</sub>H<sub>14</sub>O<sub>2</sub>)
#   * Pectin (C<sub>6</sub>H<sub>10</sub>O<sub>7</sub>)
# * Check [nutrition information](https://en.wikipedia.org/wiki/Banana#Nutrition)
# 
# ### 2.a. Which of the above components of the banana composition will contribute significantly to your answer and why?
# ### 2.b. What is the activity just from gamma radiation?
# ### 2.c. Assuming no self-shielding of electrons (all electrons produced escape the banana), what is the activity just from electrons?
# ### 2.d. What is the total activity of the banana?
# ### 2.e. When you purchase the banana, how much of the activity from the banana are you being exposed to?
# ### 2.f. When you eat the banana, how much of the activity are you being exposed to?

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


m=70
mkrad=(0.0169/1000)


# In[9]:


Mkrad=(39.963998/1000)
Nkrad=(mkrad/Mkrad)


# In[10]:


Nkrad=Nkrad*(6.02E23)


# In[11]:


who Nkrad


# In[12]:


print(Nkrad)


# In[13]:


halflife=(1.26E9)*365*24*3600


# In[14]:


decayconstant=np.log(2)/halflife


# In[15]:


print (decayconstant)


# In[16]:


activity=decayconstant*Nkrad
print("activity of human being is", activity, "Bq")


# In[17]:


specificactivity=activity/m
print("activity of self is",specificactivity,"Bq/kg")


# Mass of K-40 in 70kg human body,half-life, and sources of radiation that successfully emmit from human body obtained from: https://sciencedemonstrations.fas.harvard.edu/presentations/radioactive-human-body
# Molercular Weight of K-40 obtained from: https://pubchem.ncbi.nlm.nih.gov/compound/Potassium-40

# In[18]:


mbanana=120


# In[19]:


mvitb=120*(.0004/100)
mk=120*(.358/100)
mvitc=120*(.0087/100)


# mass of isoamyl acetate and pectin in bananas could not be found

# In[20]:


print (mvitb)


# In[21]:


Mc=12.011
Mh=1.008
Mo=15.999
Mn=14.0067
Mk=39.0983
Mvitb=8*Mc+11*Mh+Mn+3*Mo
percentcvitb=8*Mc/Mvitb
mcvitb=percentcvitb*mvitb
Ncvitb=(mcvitb/Mc)*6.02E23
Ncvitb=.001*Ncvitb
Nk=(mk/Mk)*6.02E23
Mvitc=6*Mc+8*Mh+6*Mo
percentcvitc=6*Mc/Mvitc
mcvitc=percentcvitc*mvitc
Ncvitc=(mcvitc/Mc)*6.02E23
Ncvitc=.001*Ncvitc
Ncbetarad=Ncvitb+Ncvitc
Nkbetarad=.8914*(.000117*Nk)
Nkgammarad=.1066*(.000117*Nk)


# In[23]:


khalflife=(1.26E9)*365*24*3600
chalflife=9.426E10*365*24*3600
kdecayconstant=np.log(2)/khalflife
cdecayconstant=np.log(2)/chalflife
kactivity=Nkgammarad*kdecayconstant
bananaactivity=kactivity
print("activity of 120g banana is",bananaactivity,"Bq")


# The amount of gamma radiation of potasium 40 will contribute the most since it is the only radiation actually emmitted from the banana 

# In[25]:


print("activity from gamma radiation=",bananaactivity,"Bq")


# In[26]:


betaactivity=Nkbetarad*kdecayconstant+Ncbetarad*cdecayconstant
print("activity from beta radiation =",betaactivity,"Bq")


# In[27]:


totalactivity=bananaactivity+betaactivity
print("Total activity of banana=",totalactivity,"Bq")


# In[28]:


print("When banana is purchased you are exposed to",bananaactivity,"Bq")
print("When you eat the banana you are exposed to",totalactivity,"Bq")


# 

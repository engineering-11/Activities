#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Q1a
import math
k_time = 1.26*10**9
c_time = 5730
k_atoms = 2.11*10**18
c_atoms = 6.93*10**20
k_branch = 10.66/100
c_branch = 1 
#carbon goes through Beta decay
#b is time
def lamb(a,b):
    return math.log(a)/b


# In[41]:


print(lamb(2,k_time))


# In[42]:


#x is time; y is atoms; z is Gamma branching ratio
def radioactivity(x, y, z):
    return lamb(2,x)*y*z


# In[43]:


#Activity of K
print(radioactivity(k_time, k_atoms, k_branch))


# In[44]:


#Activity of C
print(radioactivity(c_time, c_atoms, c_branch))


# In[45]:


#Q1b
# mass = 50000g
k_spec_activity = 7.04*10**-6
k_body_cont = 0.2/100
c_spec_activity = 4.5
c_body_cont = 23/100
my_mass = 50000


# In[46]:


# p is specific activity, q is body content
def activity (p, q):
    return my_mass * p * q 


# In[47]:


#Activity of K in Body
print(activity(k_spec_activity, k_body_cont))


# In[48]:


#Activity of C in Body
print('My radioactivity is:', activity(c_spec_activity, c_body_cont))


# #1c
# Sources:
# https://sciencedemonstrations.fas.harvard.edu/presentations/radioactive-human-body
# http://www.iem-inc.com/information/tools/specific-activities 

# Potassium (K)- radioactive
# Vitamin B6 (C8H11NO3) - pyridoxine 
# Vitamin C (C6H8O6)- radioactive ascorbic acid (injection?)
# Isoamyl acetate (C7H14O2) 
# Pectin (C6H10O7)

# #2a
# Potassium (K-40) would be the gratest contributor to the activity of the banana, as the content of potassium is greater than the compunds listed; the average banana contains about 358 mg of potassium. 

# In[53]:


#2b activity from Gamma ray 
banana_mass = 120
k40_mm = 40
c14_mm = 14
k40_na = 0.0117/100
c14_na = 1*10**-10/100
k40_content = 0.358/100
avogadro = 6.022*10**23
#o.422 and 118 are proportions of K to banana.
k_comp = banana_mass * k40_content 
print(k_comp)
#The total K content (g) in 120g banana


# In[54]:


k40_comp_atoms = k_comp * k40_na / k40_mm * avogadro
print('The K40 content in atoms in 120g of banana is:', k40_comp_atoms)


# In[55]:


# l is composition of atoms in banana; m is branch ratio
def radiation(l, m):
    return l * lamb(2,k_time) * k_branch
print ('Gamma radiation from the banana is:', radiation(k40_comp_atoms, k_branch))


# Only potassium goes through the gamma decay; C-14 decays through Beta decay, and thus would not affect the gamma emissions of the banana.

# In[71]:


#2c 
k_mm = 39
b6_mm = 169.08
vc_mm = 176.06
k_content = 0.358/100
b6_content = 4*10**-4/100
vc_content = 8.7*10**-3/100
k_cmpd_ratio = 1
b6_cmpd_ratio = 8
vc_cmpd_ratio = 6
k_branch_beta = 89.14/100


# In[80]:


#q- content in banana; r- molar mass; s- cmpd ratio; t- nat abundance; u- half life; v- branch ratio
def electron_activity(q, r, s, t, u, v):
    return banana_mass * q / r * s * t * lamb(2,u) * v * avogadro
print('electron activity from K40 is:', electron_activity(k_content, k_mm, k_cmpd_ratio, k40_na, k_time, k_branch_beta))


# In[83]:


print('electron activity from C14 in Vitamin B6 is:', electron_activity(b6_content, b6_mm, b6_cmpd_ratio, c14_na, c_time, c_branch))


# In[85]:


print('electron activity from C14 in Vitamin C is:', electron_activity(vc_content, vc_mm, vc_cmpd_ratio, c14_na, c_time, c_branch))


# In[86]:


k40_e_activity = 380586890.0977857
c14_e_activity = 1654.4383003135376 + 25918.069003550063


# In[89]:


banana_e_activity = k40_e_activity + c14_e_activity
print('The electron activity from the banana is:', banana_e_activity)


# In[92]:


#2d
banana_g_activity = 44375475.008204356
total_banana_activity = banana_e_activity + banana_g_activity 
print(total_banana_activity)


# #2e
# When purchasing a banana, the banana peel shields us from the activity derived from beta decay. Thus, we would only be exposed to the radiation associated with the gamma decay of potassium: 380614462.60508955 Bq

# #2f
# Consuming the banana would expose us to all forms of radiation associated with all forms of decays occuring within the banana: 424989937.6132939 Bq

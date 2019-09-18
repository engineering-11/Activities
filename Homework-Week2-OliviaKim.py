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

# In[8]:


#1a
import numpy as np
potassium_40 = 0.0117 #in percentage & natural abundance
half_life_K40 = 1.28*10**9 #y
potassium_content = 0.2 #percent
mm_K = 39.098

m = 70 * potassium_40/100 * potassium_content/100 * 1000 #units in g
p = m * 1/39.098 * 6.023 * 10**23
r = np.log(2)/(half_life_K40 * 3.15 * 10**7) * p
print(r, "Bq")


# In[12]:


#1b
specific_activity_K40 = 30.5 #Bq g-1
w = 54 * 30.5 * 1000
print(w, "Bq")


# Baes, Fred. “Hps.org.” Health Physics Society, hps.org/publicinformation/ate/faqs/faqradbods.html.
# 
# Average Dose, https://www.nrc.gov/reading-rm/basic-ref/students/for-educators/average-dose-worksheet.pdf.

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

# 2a) It would be potassium, which also contains potassium decay. Potassium contributes significantly since banana itself is contains a lot of potassium. 

# 2b) Activity from gamma radiation are about 11% of radioactivity of potassium. 

# 2c) Activity from beta are about 89% of radioacitiviy of potassium. 

# 2d) The total activity of the banana is approximately 15 Bq as it only contains about 0.5g of potassium. 

# In[16]:


#2e) When you purchase the banana: 

total_activity_banana_K40 = 15
total = 15 * 0.89
print("When you purchase the banana, you are being exposed to", total, "Bq")


# 2f) When you eat the banana, you are being exposed to approximately 0.1µSv, which is far less than the average consumption.

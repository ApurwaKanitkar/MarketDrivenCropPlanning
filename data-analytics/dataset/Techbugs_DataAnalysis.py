#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# In[3]:


df = pd.read_csv('D:\MarketDrivenCropPlanning\data-analytics\dataset\Cleaned_dataset.csv')


# In[4]:


df.head(5)


# In[5]:


Gwalior_df = df[df['Dist Name'] == 'Gwalior']


# In[9]:
# plt.figure(figsize=(10, 4))
# plt.plot(Gwalior_df['Year'], Gwalior_df['RICE AREA (1000 ha)'], marker='o', linestyle='-', color='b')
# plt.title('Rice Area Over Time in Gwalior')
# plt.xlabel('Year')
# plt.ylabel('RICE AREA (1000 ha)')
# plt.grid(True)
# plt.show()


# In[10]:


plt.figure(figsize=(10, 6))
plt.plot(Gwalior_df['Year'], Gwalior_df['RICE PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='b', label='Rice Production')
plt.plot(Gwalior_df['Year'], Gwalior_df['WHEAT PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='r', label='Wheat Production')
plt.plot(Gwalior_df['Year'], Gwalior_df['MAIZE PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='g', label='Maize Production')

plt.title('Crop Production Over Time in Gwalior')
plt.xlabel('Year')
plt.ylabel('Production (1000 tons)')
plt.grid(True)
plt.legend()

plt.show()


# # In[11]:


Pune_df = df[df['Dist Name'] == 'Pune']
plt.figure(figsize=(12, 10))
plt.plot(Pune_df['Year'], Pune_df['RICE YIELD (Kg per ha)'], marker='o', linestyle='-', color='b', label='Rice')
plt.plot(Pune_df['Year'], Pune_df['WHEAT YIELD (Kg per ha)'], marker='o', linestyle='-', color='r', label='Wheat')
plt.plot(Pune_df['Year'], Pune_df['MAIZE YIELD (Kg per ha)'], marker='o', linestyle='-', color='g', label='Maize') 
plt.plot(Pune_df['Year'], Pune_df['FINGER MILLET YIELD (Kg per ha)'], marker='o', linestyle='-', color='y', label='Finger Millet') 
plt.plot(Pune_df['Year'], Pune_df['PIGEONPEA YIELD (Kg per ha)'], marker='o', linestyle='-', color='xkcd:sky blue', label='Groundnut') 

plt.title('Crop Yeild Over Time in Pune')
plt.xlabel('Year')
plt.ylabel('Yield (Kg per ha)')
plt.grid(True)
plt.legend()

# plt.show()


# In[12]:


plt.figure(figsize=(12, 10))
plt.plot(Pune_df['Year'], Pune_df['GROUNDNUT YIELD (Kg per ha)'], marker='o', linestyle='-', color='c', label='Groundnut')
plt.plot(Pune_df['Year'], Pune_df['SUGARCANE YIELD (Kg per ha)'], marker='o', linestyle='-', color='m', label='Sugarcane')
plt.plot(Pune_df['Year'], Pune_df['SESAMUM YIELD (Kg per ha)'], marker='o', linestyle='-', color='k', label='Sesamum')

plt.title('Crop Yeild Over Time in Pune')
plt.xlabel('Year')
plt.ylabel('Yield (Kg per ha)')
plt.grid(True)
plt.legend()

# plt.show()


# In[14]:


Sehore_df = df[df['Dist Name'] == 'Sehore']
Patiala_df = df[df['Dist Name'] == 'Patiala']
Kollam_df = df[df['Dist Name'] == 'Kollam']


# In[16]:


plt.figure(figsize=(10, 6))
plt.plot(Sehore_df['Year'], Sehore_df['WHEAT YIELD (Kg per ha)'], marker='o', linestyle='-', color='b', label='Sehore')
plt.plot(Patiala_df['Year'], Patiala_df['WHEAT YIELD (Kg per ha)'], marker='o', linestyle='-', color='r', label='Patiala')
plt.plot(Kollam_df['Year'], Kollam_df['WHEAT YIELD (Kg per ha)'], marker='o', linestyle='-', color='k', label='Kollam')

plt.title('Wheat Yeild Over Time')
plt.xlabel('Year')
plt.ylabel('Yield (Kg per ha)')
plt.grid(True)
plt.legend()

# plt.show()


# In[15]:


plt.figure(figsize=(10, 6))
plt.plot(Kollam_df['Year'], Kollam_df['RICE YIELD (Kg per ha)'], marker='o', linestyle='-', color='b', label='Rice')
plt.plot(Kollam_df['Year'], Kollam_df['WHEAT YIELD (Kg per ha)'], marker='o', linestyle='-', color='r', label='Wheat')
plt.plot(Kollam_df['Year'], Kollam_df['MAIZE YIELD (Kg per ha)'], marker='o', linestyle='-', color='g', label='Maize')
plt.plot(Kollam_df['Year'], Kollam_df['GROUNDNUT YIELD (Kg per ha)'], marker='o', linestyle='-', color='c', label='Groundnut') 
plt.plot(Kollam_df['Year'], Kollam_df['SUGARCANE YIELD (Kg per ha)'], marker='o', linestyle='-', color='m', label='Sugarcane') 
plt.plot(Kollam_df['Year'], Kollam_df['FINGER MILLET YIELD (Kg per ha)'], marker='o', linestyle='-', color='y', label='Finger Millet') 
plt.plot(Kollam_df['Year'], Kollam_df['SESAMUM YIELD (Kg per ha)'], marker='o', linestyle='-', color='k', label='Sesamum') 

plt.title('Crop Yeild Over Time in Kollam')
plt.xlabel('Year')
plt.ylabel('Yield (Kg per ha)')
plt.grid(True)
plt.legend()

# plt.show()


# In[ ]:





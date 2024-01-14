#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


temp = np.random.uniform(18,42, size=30)
temp


# In[3]:


plt.plot(temp)


# In[4]:


np.random.seed(0)
temp = np.random.uniform(18,42, size=30)
plt.plot(temp)
plt.show()


# In[5]:


plt.figure(figsize=(15,5))
np.random.seed(0)
temp = np.random.uniform(18,42, size=30)
plt.plot(temp)
plt.show()


# In[6]:


plt.figure(figsize=(20,5))
np.random.seed(0)

summer = np.random.uniform(30,45, size = 30)
plt.plot(summer)

winter = np.random.uniform(15,35, size = 30)
plt.plot(winter)

rainy = np.random.uniform(20,40, size = 30)
plt.plot(rainy)
plt.show()


# In[7]:


plt.figure(figsize=(20,5))
np.random.seed(0)

summer = np.random.uniform(30,45, size = 30)
plt.plot(summer, linestyle="dotted",color="red",lw=2)

winter = np.random.uniform(15,25, size = 30)
plt.plot(winter, linestyle="dashed",color="blue",lw=3)

rainy = np.random.uniform(20,40, size = 30)
plt.plot(rainy,linestyle="dashdot",color="green",lw=4)

plt.title("Season's Change")
plt.xlabel("Day of Month")
plt.ylabel("temprature")
plt.legend(["summer","winter","rainy"],loc=3)
plt.show()


# In[8]:


values = [140,145,33,14,4]
countries = ["India","China","US","Russia","Canada"]
plt.pie(values, labels=countries)
plt.title("Citizen of World")
plt.show()


# In[9]:


np.random.seed(0)
weight_m = np.random.uniform(60,100, size = 30)
height_m = np.random.uniform(150,185,size = 30)
weight_f = np.random.uniform(30,70, size = 30)
height_f = np.random.uniform(120,155,size = 30)
plt.scatter(weight_f,height_f, color="green",marker="D")
plt.scatter(weight_m,height_m, color="Blue",marker="*")
plt.title("Height VS Weight",fontsize=15)
plt.legend(["Female", "Male"])
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()


# In[3]:


population = [140,145,33,14,4]
countries = ["India","China","US","Russia","Canada"]
plt.bar(countries,population,color="Purple",edgecolor="Yellow")#use barh to show it horizontally, remove h and it wil show vertically.
plt.title("Citizen's of the world")
plt.show()


# In[6]:


fresher = np.random.uniform(5,10, size = 50)
junior = np.random.uniform(15,20, size = 35)
senior = np.random.uniform(35,45, size = 30)
manager = np.random.uniform(55,85, size = 20)
CEO = np.random.uniform(85,95, size = 5)


# In[12]:


plt.figure(figsize=(15,7))
plt.boxplot([fresher,junior,senior,manager,CEO], 
            labels=["Fresher","Junior","Senior","Manager","CEO"],patch_artist= True, vert=1)
plt.show()


# In[13]:


somedata = np.random.uniform(25,100, size = 100)
plt.hist(somedata,bins=20, histtype="bar", color= "orange", edgecolor = "Black")
plt.show()


# In[14]:


tips = sns.load_dataset("tips")


# In[15]:


tips.head()


# In[16]:


#Setting the theme of the graphs
plt.style.use('seaborn-bright')
sns.set_style('whitegrid')


# In[18]:


sns.scatterplot(x="total_bill",y="tip",hue="day",size="size",data=tips)
plt.xlabel("Total Bill")
plt.show()


# In[28]:


sns.catplot(x="day",y="tip",data=tips,kind="violin")
plt.show()


# In[24]:


sns.jointplot(x="total_bill",y="tip",data=tips,kind="reg")
plt.show()


# In[31]:


sns.countplot(x="day",hue="time",data=tips)
plt.show()


# In[32]:


sns.pairplot(tips)
plt.show()


# In[33]:


plt.figure(figsize=(10,5))
sns.heatmap(tips.corr(),annot=True)
plt.show()


# In[34]:


sns.relplot(x="total_bill",y="tip",data=tips,col="day",row="smoker")
plt.show()


# ## Subplots

# In[35]:


plt.figure(figsize=(15,5))
plt.subplot(1,2,2) #row,column,position of plot
sns.countplot(x='day',data=tips)

plt.subplot(1,2,1)
sns.heatmap(tips.corr(),annot=True)
plt.show()


# In[ ]:





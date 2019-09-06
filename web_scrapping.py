#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd               #data frame - data to spreadsheet
import numpy as np                #manupulating data in arrays
import matplotlib.pyplot as plt   #ploting data  

get_ipython().run_line_magic('matplotlib', 'inline')

from urllib.request import urlopen #opening website
from bs4 import BeautifulSoup
import re


# In[2]:


url = "https://www.hubertiming.com/results/2018MLK"
html = urlopen(url)          #opening link to the website


# In[3]:


soup = BeautifulSoup(html)   #created an object soup that contains the information


# In[5]:


#start extracting information
print(title)
title = soup.title
print(title.text)


# In[10]:


links = soup.find_all('a', href=True)  #a - key to find
for link in links:
    print(link['href'])


# In[13]:


#getting data

allrows = soup.find_all('tr')
print(allrows[:5])


# In[15]:


#row list
allrows = soup.find_all('tr')
for row in allrows:
    row_list = row.find_all('td')
print(row_list)
for cell in row_list:
    print(cell.text)


# In[29]:


#getting data in row
data = []
allrows = soup.find_all('tr')
for row in allrows:
    row_list = row.find_all('td')
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
data = data[4:]
print(data[-2:])


# In[30]:


#other method of getting data through pandas and dataframe
df = pd.DataFrame(data)
print(data)


# In[31]:


#data in order
df = pd.DataFrame(data)
print(df)


# In[36]:


df = pd.DataFrame(data)
print(df.head(2)) #print first five column, 2- rows
print(df.tail(2))


# In[37]:


#headers
col_headers = soup.find_all('th')
col_headers


# In[38]:


#arrange header in list
header_list = []
col_headers = soup.find_all('th')
for col in col_headers:
    header_list.append(col.text)
print(header_list)


# In[39]:


#headers in pandas
df.columns = header_list
print(df.head())


# In[40]:


#to check info in the columns
df.info()


# In[41]:


df.shape     #check shape (enteries, column)


# In[62]:


df2 = df.dropna(how='any')
df2.shape


#!/usr/bin/env python
# coding: utf-8

# # BS4

# In[15]:


import pandas as pds
from bs4 import BeautifulSoup


# In[56]:


with open(r"C:\Users\RAJSHREE\Downloads\1482-1\OG\geographical\CTRY_GB.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


# In[57]:


soup


# #### Bs4 parser is not able to parse the whole html doc

# # With selenium

# In[110]:


import os
import selenium
from selenium import webdriver
import io
import requests
from selenium.webdriver.common.by import By


# In[111]:


driver = webdriver.Chrome()


# In[101]:


driver.get(r"C:\Users\RAJSHREE\Downloads\1482-1\OG\geographical\CTRY_GB.html")


# #### The below xpath is showing as NoSuchElementException error (it's a table tag in html page )

# In[92]:


table = driver.find_element_by_xpath("/html/body/div/table[1]/tbody")


# ### Trying Sample website to check any other xpath is working

# In[112]:


driver.get(r"https://bulkdata.uspto.gov/data/patent/officialgazette/2021/")


# In[103]:


table = driver.find_element_by_xpath("//*[@id=\"usptoGlobalHeader\"]/div[3]/table[2]")


# In[113]:


element = driver.find_element_by_xpath("//*[@id=\"uspto-header-links\"]/span[1]/a")


# In[114]:


element.click()


# ### It's working with any other xpath (or table tag)

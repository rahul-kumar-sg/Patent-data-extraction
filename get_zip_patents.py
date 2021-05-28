#!/usr/bin/env python
# coding: utf-8

# In[40]:


import requests
from bs4 import BeautifulSoup
import requests, zipfile, io


# In[7]:


url = 'https://bulkdata.uspto.gov/data/patent/application/redbook/fulltext/2021/'


# In[8]:


page = requests.get(url)


# In[16]:


soup = BeautifulSoup(page.text, 'html.parser')


# In[33]:


download_urls = []


for link in soup.find_all('a'):
    
    if '.zip' in link['href']:
        download_urls.append(url + link['href'])


# In[38]:


for download_url in download_urls:
    r = requests.get(download_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()


# In[41]:





# In[42]:





# In[ ]:





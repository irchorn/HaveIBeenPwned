#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[37]:


API_key = "dd52114a22ca4f08b46da0870bf39497"
URL = "https://haveibeenpwned.com/api/v3/breachedaccount/{irchorn@gmail.com} hipb-api-key = "+API_key+""
response = requests.get(URL)
print(response.status_code)
response.text


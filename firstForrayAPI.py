#!/usr/bin/env python
# coding: utf-8

# In[52]:


import requests


# In[53]:


import json


# In[54]:


import pandas as pd


# In[35]:


people = requests.get('http://api.open-notify.org/astros.json')
people.text


# In[29]:


people_json  = people.json()
people_json


# In[9]:


len(people_json['people'])


# In[36]:


starship9 = requests.get("https://swapi.co/api/starships/9/")
starship9_json = starship9.json()
starship9_json


# In[43]:


sw_data = requests.get("https://swapi.co/api/people/")
sw_data_json = sw_data.json()


# In[44]:


sw_data_json


# In[55]:


sw_folks_pandas = pd.DataFrame(sw_data_json['results'])
sw_folks_pandas


# In[48]:


sw_species = requests.get("https://swapi.co/api/species/")
sw_species_json = sw_species.json()


# In[50]:


sw_species_json


# In[57]:


sw_species_pandas = pd.DataFrame(sw_species_json['results'])
sw_species_pandas


# In[ ]:





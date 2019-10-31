#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Link = https://howpcrules.com/step-by-step-guide-on-scraping-data-from-a-website-and-saving-it-to-a-database/
#Importing libraries
import requests #for making HTTP requests in Python
import MySQLdb #for linking to scraped data to SQL
from bs4 import BeautifulSoup #for data scraping itself


# In[24]:


#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "Bella Ghazaryan"
PASSWORD = "Bella2019"
DATABASE = "scraping_sample"


# In[25]:


list_url=['https://en.wikipedia.org/wiki/Avengers_(comics)',
          'https://en.wikipedia.org/wiki/The_Avengers:_Earth%27s_Mightiest_Heroes',
          'https://en.wikipedia.org/wiki/The_Avengers:_United_They_Stand',
          'https://en.wikipedia.org/wiki/Avengers:_Age_of_Ultron',
          'https://en.wikipedia.org/wiki/Avengers:_Endgame']


# In[26]:


i_length=len(list_url)


# In[27]:


results={}


# In[35]:


for i in range(0,i_length):
    url=list_url[i]
    plain_html_text = requests.get(url)
    html_page = plain_html_text.content
    soup = BeautifulSoup(html_page, 'html.parser')
    the_word = 'Avengers'
    text1 = soup.find_all('h1', text=lambda t: t and the_word in t)
    results[url]=text1
    #print(soup.text.strip())
    #output = ''
#    blacklist = [
#        '[document]',
#        'noscript',
#        'header',
#        'html',
#        'meta',
#        'head', 
#        'input',
#        'script',
#        'search',
        # there may be more elements you don't want, such as "style", etc.
#    ]

#for t in text1:
#	if t.parent.name not in blacklist:
#		output += '{} '.format(t)


# In[7]:


for i in range(0,i_length):
    url=list_url[i]
    plain_html_text = requests.get(url)
    html_page = plain_html_text.content
    soup = BeautifulSoup(html_page, 'html.parser')
    the_word = 'Avengers'
    text1 = soup.find_all('h1', text=lambda t: t and the_word in t)
    results[url]=text1
    #print(soup.text.strip())
    output = ''
#    blacklist = [
#        '[document]',
#        'noscript',
#        'header',
#        'html',
#        'meta',
#        'head', 
#        'input',
#        'script',
#        'search',
        # there may be more elements you don't want, such as "style", etc.
#    ]

#for t in text1:
#	if t.parent.name not in blacklist:
#		output += '{} '.format(t)


# In[36]:


#for url, text1 in results.items():
#    print (url)
print (results)


# In[37]:


for url, text1 in results.items():
    print (str(url) + ':' + str(text1))
#print (results['https://en.wikipedia.org/wiki/The_Avengers:_Earth%27s_Mightiest_Heroes'])


# In[38]:


records= []
for result in results:
    Scraped_url=url
    Scraped_text=text1
    records.append((Scraped_url, Scraped_text))


# In[39]:


import pandas as pd
df=pd.DataFrame(records, columns=['Scraped url', 'Scraped text'])


# In[12]:


#df.head()


# In[40]:


import pandas as pd
df=pd.DataFrame.from_dict(results)


# In[19]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





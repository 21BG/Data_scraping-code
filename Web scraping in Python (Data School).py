#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Reading the web page into Python


# In[2]:


#Allows reading htmpl into Python
import requests

#If don't have it, go "pip install requests" in Anaconda Promt or Control Panel

r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')


# In[4]:


#print the first 500 characters of the HTML
print(r.text[0:500])


# In[10]:


#Parsing the HTML using Beautiful Soup
#If don't have it, go "pip install bs4" in Anaconda Promt or Control Panel


# In[13]:


from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')

#BeautifulSoup reads html and making sence of its structure using html.parser


# In[14]:


#Collecting all the records
#<span class="short-desc"><strong>DATE</strong>LIE <span class="short-truth"><a href="LINK TO THE TRUE" target="_blank">EXPLANATION</a></span></span>


# In[15]:


results=soup.find_all('span', attrs={'class':'short-desc'})


# In[16]:


len(results)


# In[17]:


results[0:3]
#displaying first 3 results


# In[18]:


results[-1]


# In[19]:


#Extraction the date (Manualy)


# In[21]:


first_result=results[0]
first_result


# In[22]:


first_result.find('strong')


# In[23]:


first_result.find('strong').text
#escape sequence


# In[24]:


first_result.find('strong').text[0:-1]


# In[26]:


first_result.find('strong').text[0:-1]+', 2017'


# In[27]:


#Extract_result_for_the_lie


# In[28]:


first_result


# In[29]:


first_result.contents


# In[30]:


first_result.contents[1]


# In[33]:


first_result.contents[1][1:-2]
#Good way to clean your entires


# In[34]:


#Extracting the explanation


# In[ ]:


#Option of extracting 1


# In[35]:


first_result.contents[2]


# In[36]:


first_result.contents[2].text


# In[43]:


first_result.contents[2].text[1:-1]


# In[39]:


#Option of extracting 2


# In[40]:


first_result.find('a')


# In[41]:


first_result.find('a').text


# In[44]:


first_result.find('a').text[1:-1]


# In[45]:


#Extracting the url


# In[51]:


first_result.contents[2]


# In[52]:


first_result.find('a')


# In[53]:


first_result.find('a')['href']


# In[55]:


records= []
for result in results:
    date=result.find('strong').text[0:-1]+', 2017'
    lie=result.contents[1][1:-2]
    explanation=result.contents[2].text[1:-1]
    url=result.find('a')['href']
    records.append((date, lie, explanation, url))


# In[56]:


len(records)


# In[57]:


records[0:3]


# In[58]:


#Applying a tabular data structure


# In[63]:


import pandas as pd
df=pd.DataFrame(records, columns=['Date', 'Lie', 'Explanation', 'URL'])


# In[64]:


df.head()


# In[65]:


df.tail()


# In[68]:


df['Date']=pd.to_datetime(df['Date'])


# In[69]:


df.head()


# In[73]:


#Exporting the dataset to CSV file


# In[70]:


df.to_csv('trump_lies.csv', index=False, encoding='utf-8')


# In[72]:


df=pd.read_csv('trump_lies.csv',parse_dates=['Date'],encoding='utf-8')


# In[ ]:





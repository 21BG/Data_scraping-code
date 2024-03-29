#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://howpcrules.com/step-by-step-guide-on-scraping-data-from-a-website-and-saving-it-to-a-database/

import requests
import MySQLdb
from bs4 import BeautifulSoup


# In[2]:


#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = ""
DATABASE = "scraping_sample"


# In[3]:


#scrape the same page twice. If you are planning to scrape multiple pages with a similiar design, use "i" to generate different urls.
for i in range(0, 2):
    #URL to be scraped
    url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
    #Load html's plain data into a variable
    #plain_html_text = requests.get(url_to_scrape)
    plain_html_text = requests.get(list_url[i])
    #parse the data
    soup = BeautifulSoup(plain_html_text.text, "html.parser")


# In[4]:


#print the whole html data to screen
#print(soup.prettify())


# In[5]:


#Get the name of the class
name_of_class = soup.h3.text.strip()


# In[6]:


#Get all data associated with this class
basic_data_table = soup.find("table", {"summary": "Basic data for the event"});
#Get all cells in the base data table
basic_data_cells = basic_data_table.findAll('td')


# In[7]:


#get all the different data from the table's tds
type_of_course = basic_data_cells[0].text.strip()
lecturer = basic_data_cells[1].text.strip()
number = basic_data_cells[2].text.strip()
short_text = basic_data_cells[3].text.strip()
choice_term = basic_data_cells[4].text.strip()
hours_per_week_in_term = basic_data_cells[5].text.strip()
expected_num_of_participants = basic_data_cells[6].text.strip()
maximum_participants = basic_data_cells[7].text.strip()
assignment = basic_data_cells[8].text.strip()
lecture_id = basic_data_cells[9].text.strip()
credit_points = basic_data_cells[10].text.strip()
hyperlink = basic_data_cells[11].text.strip()
language = basic_data_cells[12].text.strip()
#To save data
#Save class's base data to the database
# Open database connection
db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
try:
 # Execute the SQL command
 cursor.execute(sql)
 # Commit your changes in the database
 db.commit()
except:
 # Rollback in case there is any error
 db.rollback()
 #get the just inserted class id
sql = "SELECT LAST_INSERT_ID()"
try:
 # Execute the SQL command
 cursor.execute(sql)
 # Get the result
 result = cursor.fetchone()
 # Set the class id to the just inserted class
 class_id = result[0]
except:
 # Rollback in case there is any error
 db.rollback()
 # disconnect from server
 db.close()
 # on error set the class_id to -1
 class_id = -1


# In[8]:


#Get the tables where the dates are written.
dates_tables = soup.find_all("table", {"summary": "Overview of all event dates"});


# In[9]:


#The part with SQL can be found https://howpcrules.com/step-by-step-guide-on-scraping-data-from-a-website-and-saving-it-to-a-database/


# 

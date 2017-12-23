# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on Wed Jul 26 13:03:43 2017

@author: Sahir Noor Ali

@Code: Personality Insights 

@Pre-Req: Make sure that the WDC SDK is installed before the code is executed.
          The following command on the command prompt will ensure it:
              
              pip install --upgrade watson-developer-cloud
              
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#--------------------------------------------------------------
#Imports
#--------------------------------------------------------------

#The PersonalityInsights class from WDC
from watson_developer_cloud import PersonalityInsightsV3

#Pandas for data handling
import pandas as pd

#Time class to measure the time taken
import time
#--------------------------------------------------------------

#Read the data
data = pd.read_csv('Reviews.csv')

#Make a copy of 10 rows for smaller testing
small_data = data.head(100).copy()

#To view the documentation
#print(help(PersonalityInsightsV3))

#-------------------------------------------------------------------------
#Instantiate TA Object with your Credentials
#-------------------------------------------------------------------------
PI = PersonalityInsightsV3( 
    username='c7a75b81-5b15-4168-87c5-cdafb5f9f002',
    password='AYMszHcgNPNw',
    version='2016-10-20',
    url = 'https://gateway.watsonplatform.net/personality-insights/api')
#-------------------------------------------------------------------------

#Get the current time on the clock
time_start = time.clock()

#-------------------------------------------------------------------------
#Iterate Over All the Reviews and Append the Result:
#-------------------------------------------------------------------------    
for index, review in small_data['Text'].iteritems():
    
    #Get the words in the review
    count = len(review.split()) 
    
    #Check if it's greater than 100
    if count >= 100:
    
        #Enough words to feed into PI
        #Pass on the review to PI
        json_output = PI.profile(review,content_type='text/plain')

        #Iterate over the result (having heirarchy)
        for i in json_output['personality']:
            for j in i['children']:
                #Append the attributes to the data
                small_data.set_value(index, j['name'], j['percentile']) 
                        
        for i in json_output['needs']:
            #Append the attributes to the data
            small_data.set_value(index, i['name'], i['percentile']) 
            
        for i in json_output['values']:
            #Append the attributes to the data
            small_data.set_value(index, i['name'], i['percentile']) 
#-------------------------------------------------------------------------

#Get the current time again and subract from 
#previous to measure the time taken        
time_end = time.clock() - time_start

#Print the time taken
print(time_end)
                
#Save the enriched data to another CSV File
small_data.to_csv('OutputPI.csv')



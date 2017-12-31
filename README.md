# Enriching data with IBM Personality Insights

## Introduction
IBM Personality Insights (https://www.ibm.com/watson/services/personality-insights/) is one of the cognitive services
provided by IBM Cloud. It can help us predict personality characteristics, needs and values if the text written by the respective
users is passed onto the service as input.

## Dataset
The dataset enriched in this project is taken from Kaggle:

https://www.kaggle.com/snap/amazon-fine-food-reviews

## Process
Every review is passed to an instance of IBM Watson Personality Insights at IBM Cloud (https://www.ibm.com/cloud/) which was
formerly known as Bluemix. The result of the API call is then parsed from JSON and appended as columns in the data frame which
is then written into another CSV. The output CSV is uploaded along with the Project to make it clear as how it's adding more 
meaning to the original data. However, the dataset can be downloaded from the link since it's more than 250MB.

## Note 
Make sure to enter your personal service credentials (username and password) along with the URL mentioned for your instance in the IBM Cloud. 

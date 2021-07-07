#!/usr/bin/env python3 

# trying to set up api

# importing 'requests' module to work 
# requests documentation at https://docs.python-requests.org/en/master/
import requests
import json


# geting questions request from stackoverflow
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow') 
# Print the response code  
print(response)

# Print the response with json method  
# print(response.json())

# geting titles of questions 
for question in response.json()['items']:
	print(question['title'], '\n')

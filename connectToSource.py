#This space is to pull in data for project

#libraries
import numpy as np
import pandas as pd
import os  

#Location and testing variables
#print(os.getcwd())
#Set up Secure connection

#import data into pandas dataframe
#Setting file path to a string variable
file_path = "Job_Application_Tracker.csv"
print(file_path)
applicationsStatus = pd.read_csv(file_path)

#Push data to next notebook for transformations
headers = applicationsStatus.columns.tolist()
print
#applicationsStatus.head()
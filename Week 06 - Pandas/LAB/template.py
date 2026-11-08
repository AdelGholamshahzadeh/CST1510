"""
RECORD CHECK  -  my version
===========================

Name  : Adel Gholamshahzadeh
Lane  :  AI 
Date  : 8/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

data = {
    "labeL": ["Record-1","Record-2","Record-3","Record-4","Record-5"],
    "value": [2,111,90,50,1],
    "limit": [100,100,100,100,100]
}
data_df = pd.DataFrame(data)        #adding the created dictionary as a data frame
data_file = data_df.to_csv("Record_Data.csv")   #saving it to a file as instructed
df = pd.read_csv("Record_Data.csv")         #reading the file 


df["percent"] = (df.value / df.limit) * 100         #adding a percent column
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK"  #adding a status column using the lambda function
)


print(df[(df["status"] == "OVER LIMIT") | (df["status"] == "WARNING")]) #printing with two conditions

grouped = df.groupby(by= "status")      #grouping the data by status in alphabetical order
print(grouped.value_counts())           #counting the unique values 


# importing packages
import pandas as pd
import requests
import json
import time
from glob import glob
from os.path import splitext, basename
from random import random

# Exponential Backoff Function

def exponentialbackoff(num): 
    return (2**num) + random()
  
# Initialising empty Dataframe
Mdf = pd.DataFrame()

# URL to request
## specific to this project but can 
## be modified by changing the subreddit
## name (See "subreddit=cryptocurrencymemes" 
## in url). Can also change requested metadata
## refer to PushShift documentation (link in
## README.md. 
## 500 items was max item limit at the time
## important that the url ends with "before="
## using this to go back in time

url= "https://api.pushshift.io/reddit/search/submission/?subreddit=cryptocurrencymemes&size=500&fields=created_utc,title,url,full_link&sort_type=created_utc&before="

# Initialise UTC, used most recent post's utc
utc = 1636335595 

# Scraping function
def scrape(utc):
    counter = 0
    while True: 
        counter+=1
        tempurl= url+str(utc)
        response = requests.get(tempurl)
        # print(response.status_code) 
        # ^ Check. 200 = request worked, other codes: http.cat
        df = pd.json_normalize(response.json(), record_path=['data']) # convert json to df
        if df.size == 0: 
            Mdf.to_csv("MainDF.csv")
            exit # Reaching end of subreddit condition
        filepath = "tempdfs/"+ str(counter) + ".csv"
        df.to_csv(filepath)
        Mdf.append(df)
        utc = df["created_utc"].values[-1] # Create new UTC value 
        time.sleep(exponentialbackoff(counter%5)) # Exponential backoff to avoid request blocks
        
        

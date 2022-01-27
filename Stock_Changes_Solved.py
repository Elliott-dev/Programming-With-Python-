#!/usr/bin/env python
# coding: utf-8

# In[252]:


# Import the 'os' and 'csv' libraries
import os 
import csv
import numpy as np


# In[253]:


filepath = os.path.join('..', 'Resources', 'S&P_500_5yr_stock_data.csv')


# In[255]:


# Open a connection to the comma-delimited csv file 
with open (filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    # Create variables to save our output row as printrow and greatest daily percent change as max_pct
    printrow = []
    percent_change_added_to_dict = []
    all_percent_change = []
    max_pct = 0
    
   # Iterate through each row
   # For each row, calculate the daily percent change
    for row in reader:
        percent_change = (float(row['Close'])-float(row['Open']))/float(row['Open'])*100
        row.update({'stock_change':percent_change})
        percent_change_added_to_dict.append(row)
        all_percent_change.append(percent_change)
        max_pct = max(all_percent_change)
    
   # Check if the absolute daily percent change is greater than the previous daily percent change.
   # If true, store new greatest daily percent change and printrow 
    for each_row in percent_change_added_to_dict:
        if max_pct <= each_row['stock_change']:
            printrow.append(each_row)
     
    date = printrow[0]['Date']
    open_price = printrow[0]['Open']
    high_price = printrow[0]['High']
    low_price = printrow[0]['Low']
    close_price = printrow[0]['Close']
    volume = printrow[0]['Volume']
    stock_change = round(printrow[0]['stock_change'],2)
    
    # Print out the date, stock high, stock low, volume and percent change for the day with the greatest percent change
    
    print("""The day with the greatest daily percent change was {} on that day the stock changed {}%.\nThe high of that day was {}, the low of that day was {}.\nThe volume for that day was {}.""".format(date, stock_change, high_price, low_price, volume))


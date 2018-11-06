# Project Completed by Brian Stanwood, Minhquan Nguyen, Luke Deviney, Liam Byrne on 4/17/2018
# This project finds the past Bitcoin values from spreedsheet "BTC.csv" and predicts its average for the future as well
#   as displays graphical current results found. 

# Step 1
###### importing 
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import re

############# Import file and assign date and open(price) column using pandas
bitcoin = pd.read_csv("BTC.csv")    
bitcoin["dateIndex"] = bitcoin["date"].index
bitcoin.head()
X = bitcoin["dateIndex"]
Y = bitcoin["open"]


# In[49]:

# finds average price for red line plot (predicted price line)
averagePrice = sum(Y) / len(Y)
x_predict = pd.DataFrame([[X[0]], [len(X)]])
y_predict = pd.DataFrame([[Y[0]], [len(Y)]])
x = np.array(x_predict)
y = np.array(y_predict)

############# find slope and intercept of line for calculations using linear regression from scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(x[:,0],y[:,0])

# In[58]:

# Step 2
# makes grid and plots points/line
#### plot graph with blue dots (data marks) and red line (average estimate line) with matplotlib
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.plot(x, y, "r-")
plt.plot(X, Y, "b.")
plt.xlabel("$Time (inDays)$", fontsize=16)
plt.ylabel("$Price$", rotation=0, fontsize=16)
plt.axis([0, 2000, 0, 30000])
plt.show()


# Step 3
############################ user interface portion
dateOrPrice = 1
print('Welcome to Bitcoin Average Calculator, Please choose a date or amount you would like predicted.')
while dateOrPrice != 3:
    print('1 - Enter a date')
    print('2 - Enter a price')
    print('3 - Exit')
    dateOrPrice = input('Please enter 1-3: ')
    
    # find price by date
    if dateOrPrice == '1':
        date = input('Enter date (MM/DD/YYYY) to see what price it could be: ')
        ######################## date conversion and projected day estimation for price 
        added = 0
        dateArray = re.split('/', date)
        if float(dateArray[2]) >= 2013:
            added = (float((dateArray[2])) - 2013) * 265
            if float(dateArray[0]) >= 4:
                added = added + (float(dateArray[0]) - 4) * 30
            else:
                added = added + (float(dateArray[0]) + 4) * 30
            if float(dateArray[1]) >= 28:
                added = added + (float(dateArray[0]) - 28)
            else:
                added = added + (float(dateArray[0]) + 28)      
        else:
            print('Date given is before Bitcoin timeframe.')
        hitPrice = float(added) * float(slope) + intercept
        print('The price of the Bitcoin estimated average is around ' , '${:,.2f}'.format(hitPrice) , 'at that time.\n')
        
    # find day by price 
    elif dateOrPrice == '2':
        price = input('Enter a price to see what day it may occur: $')
        price = price.replace(",", "")
        hitDate = (float(price)-intercept)/float(slope)
        print('The day Bitcoin will hit this average price is approximately : ' , (int(hitDate)), ' days from 4/28/2013.\n')

    # exit    
    elif dateOrPrice == '3':
        break
    
    
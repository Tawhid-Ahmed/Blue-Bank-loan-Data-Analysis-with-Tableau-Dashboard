# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 08:41:31 2022

@author: ASUS
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


json_file = open('loan_data_json.json') 

data=json.load(json_file)


# with open('loan_data_json.json') as jason_file:
#     data=json.load(json_file)
#     print(data)

#transform to dataframe

loandata = pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()


loandata["AnnualIncome"]= np.exp(loandata['log.annual.inc'])



length= len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category <600:
            cat=' Poor' 
        elif category >= 600 and category<680:
            cat=' Fair'     
        elif category >= 680 and category<730:
            cat='Good'
        elif category >= 730: 
            cat='Excellent'
        else:
            cat = 'Unknown'
    except:
           cat = 'Error - Unknown'         
    ficocat.append(cat)    

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat         



loandata.loc[loandata['int.rate']>0.12, 'int.rate.type' ]= "High"
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type' ]= "Low"        


catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'orange')
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar( )
plt.show()

ypoint = loandata['AnnualIncome']
xpoint= loandata['dti']
plt.scatter(xpoint, ypoint, color='green')
plt.show()


loandata.to_csv("loan_cleaned.csv", index = True)

































        
        
        
        
        
        
        
        
        
        
        
        
        
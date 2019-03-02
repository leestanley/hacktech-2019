#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:03:06 2019

@author: shriramgharpure
"""
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
ticker = input("Please specify a stock ticker.")
company = input("Please specify a company.")
numShares = input("Please specify a given number of shares.")
sharePrice = input("Please input a share price.")

NASDAQStocks = pd.read_csv('/Users/shriramgharpure/Downloads/NASDAQValidation.csv')
listValidSymbols = NASDAQStocks['Symbol']
portfolioChecker = pd.read_csv('/Users/shriramgharpure/Downloads/TestOne.csv')
portfolioTicker = portfolioChecker['Ticker']
with open("BlankPortfolio.csv", "w") as csvFile:
    bpWrite = csv.writer(csvFile)
    for i in range(len(portfolioChecker)):
        if(portfolioChecker['Ticker'][i] in listValidSymbols.values):
            bpWrite.writerow([ticker, company, numShares, sharePrice])

            
    

           
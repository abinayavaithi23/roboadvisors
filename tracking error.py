# Initial risk statistics example  

import pandas_datareader.data as web 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

def download_etf(symbol,source,start_date='2010-01-01',end_date='2022-10-01'):  
    '''
    symbol: "DJUSRE",   
    source: "stooq",    
    start_date: ... 
    end_date: ... 

    return: data (pd.DataFrame)
    '''
    data = web.DataReader(symbol,source,start=start_date,end=end_date) 
    data = data.sort_index() 

    return data 

def download_etfs(symbols,source,start_date='2010-01-01',end_date='2022-10-01'):  
    '''
    symbols is a list of ETF symbols

    symbols = ['REZ','ICF','VNQ'] 
    '''
    
    dfs = [] # empty list of pandas dataframes 

    for sym in symbols: 
        df = download_etf(sym,source,start_date=start_date,end_date=end_date)
        tmpdf = df['Close']
        dfs.append(tmpdf)  

    df = pd.concat(dfs,axis=1) 
    df.columns = symbols 

    return df 

def tracking_error(index,etf): 
    '''
    index, etf: pandas dataframes of returns with dates that are aligned 
    '''

    n = len(index) 

    tracking_error = np.sqrt(sum((index - etf)**2)/(n-1))

    return tracking_error
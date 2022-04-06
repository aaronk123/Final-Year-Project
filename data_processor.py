from doctest import master
from turtle import left
import pandas as pd
import numpy as np

def get_master_data():

    df = pd.read_csv('master_data.csv')
    return df

def read_new_data():

    df = pd.read_csv('daft properties.csv')
    return df

def update_data():

    master_df = pd.read_csv('master_data.csv', header=0) # retain the headers
    scraped_df = pd.read_csv('daft properties.csv', header=0)     
   
    # Add new houses
    master_df = add_new_entries(master_df, scraped_df)
    print('added')


def add_new_entries(master_df, scraped_df):

    master_df=scraped_df
    master_df.to_csv('master_data.csv')
    
    return master_df

update_data()

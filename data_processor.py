import pandas as pd
import numpy as np

def get_master_data():

    df = pd.read_csv('master_data.csv')
    return df

def read_new_data():

    df = pd.read_csv('daft properties.csv')
    return df

def update_data():

    master_df = get_master_data()
    scraped_df = read_new_data()

    
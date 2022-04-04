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

    

    

    # houses still for sale
    in_both = scraped_df.merge(master_df, on="daft_link", indicator=True, how='left').loc[
        lambda x: x['_merge'] == 'both']
    # print(in_both)
    # with open("still_for_sale.txt", "w") as output:
    #     print(in_both.to_string(), file=output)

    
   # print(other)

    # Remove sold properties
    # print('removing')
    # master_df = remove_entries(master_df, scraped_df)
    # print(master_df)
    # print('removed')

    # Add new houses
    print('adding')
    print(master_df)
    master_df = add_new_entries(master_df, scraped_df)
    print('added')
    print(master_df)

def remove_entries(master_df, scraped_df):

     # sold houses
    only_in_master_not_in_scraped = master_df.merge(scraped_df, on="daft_link", indicator=True, how='left').loc[
        lambda x: x['_merge'] != 'both']
    # print(only_in_master_not_in_scraped)
    # with open("sold.txt", "w") as output:
    #     print(only_in_master_not_in_scraped.to_string(), file=output)
    print(only_in_master_not_in_scraped)

    condition = master_df['daft_link'].isin(only_in_master_not_in_scraped['daft_link'])
    master_df=master_df.drop(master_df[condition].index, inplace = True)

    
    return master_df


def add_new_entries(master_df, scraped_df):

    # new houses
    only_in_scraped_not_in_master = scraped_df.merge(master_df, on="daft_link", indicator=True, how='left').loc[
        lambda x: x['_merge'] != 'both']
    # print(only_in_scraped_not_in_master)
    # with open("new.txt", "w") as output:
    #     print(only_in_scraped_not_in_master.to_string(), file=output)
    print('below is scraped only')
    print(only_in_scraped_not_in_master)
    master_df=master_df.append(only_in_scraped_not_in_master)
    
    return master_df

update_data()

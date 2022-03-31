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

    master_df = get_master_data()
    scraped_df = read_new_data()

    ##########################################################
    # To do 
    # Remove what isnt in the new df from the old df
    # Append new houses from new df to old df
    # Update existing entries for price increases/decreases
    ##########################################################

    i=0
    
    # while i< len(scraped_df):
    #     j=0
    #     while j< len(master_df):
    #         if ((master_df.iloc[j].daft_link)==(scraped_df.iloc[i].daft_link)):
    #             print('hit')
            
    #         j=j+1
    #     i=i+1
        
    ####################################

    # master_df.set_index("daft_link")
    # scraped_df.set_index("daft_link")

    all_entries_df = pd.merge(master_df, scraped_df, on="daft_link", how="outer", indicator="True")

    #in_master_not_in_new_scraped_df = all_entries_df.loc[lambda x: x['_merge'] == 'left_only']

    in_master_not_in_new_scraped_df = master_df.merge(scraped_df, left_on="daft_link", right_on="daft_link")
    other = scraped_df.merge(master_df, left_on="daft_link", right_on="daft_link")

    # not_in_master_in_scraped_df = all_entries_df.loc[lambda x: x['_merge'] == 'right_only']

    
    print(other)

    # Remove sold properties
    master_df = remove_entries(master_df, scraped_df)
    print('done')

    # Add new houses
    scraped_df = add_new_entries(master_df, scraped_df)


def remove_entries(master_df, scraped_df):

    i=0
    while (i<len(scraped_df.index)):

        ###############################
        # identify duplicate entries ##
        ###############################

        #print(master_df.iloc[i].daft_link)
        # if ((master_df.iloc[i].daft_link)==(scraped_df.iloc[i].daft_link)):
        #     print('hit')

        # link = master_df.daft_link[i]
        # my_flag = scraped_df[scraped_df.eval('link == {}'.format(link))].flag
        # print(my_flag)

        #print(master_df.iloc[i])


        i+=1
    return master_df



def add_new_entries(master_df, scraped_df):
    
    return master_df

update_data()

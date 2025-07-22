import pandas as pd
import numpy as np


kotak_alpha = pd.read_csv('Data_Replicate_Fund/Alpha_Fund/june_30/kotak_alpha_june_30.csv')
bandhan_alpha = pd.read_csv('Data_Replicate_Fund/Alpha_Fund/june_30/bandhan_alpha_june_30.csv')
mirae_alpha = pd.read_csv('Data_Replicate_Fund/Alpha_Fund/june_30/mirae_alpha_june_30.csv')
tata_alpha = pd.read_csv('Data_Replicate_Fund/Alpha_Fund/june_30/tata_alpha_june_30.csv')
stock_prices=pd.read_csv('Data_Replicate_Fund/Alpha_Fund/june_30/alpha_stock_price.csv')
common_list = []

alpha_funds_mix = pd.concat([kotak_alpha, bandhan_alpha, mirae_alpha, tata_alpha], ignore_index=True)

common_sorting_alpha_funds = alpha_funds_mix.duplicated(keep=False)

common_alpha_funds = alpha_funds_mix[common_sorting_alpha_funds]

common_positive_alpha_funds=common_alpha_funds[common_alpha_funds['stock_change'] > 2.00]

alpha_funds = common_positive_alpha_funds.drop_duplicates(subset=['stock_name'])

alpha_funds_with_high_low = pd.merge(alpha_funds,stock_prices,on='stock_name', how='inner')





for rows in alpha_funds_with_high_low.itertuples():
    print(f"Buy {rows.stock_name} if you get it at {rows.stock_low*1.15:.2f} to {rows.stock_high*0.80:.2f} for maximum returns.\n")





  



"""
1)make combined list and then find common and positive stocks
"""
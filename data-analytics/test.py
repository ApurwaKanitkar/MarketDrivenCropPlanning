import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from flask import Flask, send_file
import matplotlib.pyplot as plt
import numpy as np

# Assuming your CSV is named 'data.csv'
df = pd.read_csv('D://MarketDrivenCropPlanning//data-analytics//dataset//Cleaned_dataset.csv')
access_df = pd.read_csv('D://MarketDrivenCropPlanning//data-analytics//dataset//render1.csv')  # Assuming your access data CSV is named 'access.csv'

district_options = list(df['Dist Name'].unique())
selected_district = st.selectbox("Select District:", ['Please select']+district_options)



def get_crop_combinations(selected_district):
  global combo1crop1, combo1crop2, combo2crop1, combo2crop2
  if selected_district == 'Please select':
    pass
  else:
    combo1crop1 = access_df.loc[access_df["District"] == selected_district, "Combination_1_Crop_1"].values[0]
    combo1crop2 = access_df.loc[access_df["District"] == selected_district, "Combination_1_Crop_2"].values[0]
    combo2crop1 = access_df.loc[access_df["District"] == selected_district, "Combination_2_Crop_1"].values[0]
    combo2crop2 = access_df.loc[access_df["District"] == selected_district, "Combination_2_Crop_2"].values[0]
get_crop_combinations(selected_district)

def yield_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2):
  if selected_district == 'Please select':
    pass
  else:
    dist_df = df[df['Dist Name'] == selected_district]
    yield1 = combo1crop1 + ' YIELD (Kg per ha)'
    yield2 = combo2crop2 + ' YIELD (Kg per ha)'
    yield3 = combo2crop1 + ' YIELD (Kg per ha)'
    yield4 = combo2crop2 + ' YIELD (Kg per ha)'

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 2))

    ax1.plot(dist_df['Year'], dist_df[yield1], marker='o', linestyle='-', color='g', label=yield1)
    ax1.plot(dist_df['Year'], dist_df[yield2], marker='o', linestyle='-', color='y', label=yield2)
    ax1.set_title('Yield over time for Crop Combination 1')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Yield (Kg per ha)')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(dist_df['Year'], dist_df[yield3], marker='o', linestyle='-', color='b', label=yield3)
    ax2.plot(dist_df['Year'], dist_df[yield4], marker='o', linestyle='-', color='xkcd:sky blue', label=yield4)
    ax2.set_title('Yield over time for Crop Combination 2')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Yield (Kg per ha)')
    ax2.grid(True)
    ax2.legend()

    plt.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.1)
    st.pyplot(fig)

def price_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2):
  if selected_district == 'Please select':
    pass
  else:
    dist_df = df[df['Dist Name'] == selected_district]
    price1 = combo1crop1 + ' HARVEST PRICE (Rs per Quintal)'
    price2 = combo1crop2 + ' HARVEST PRICE (Rs per Quintal)'
    price3 = combo2crop1 + ' HARVEST PRICE (Rs per Quintal)'
    price4 = combo2crop2 + ' HARVEST PRICE (Rs per Quintal)'

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 2))

    ax1.plot(dist_df['Year'], dist_df[price1], marker='o', linestyle='-', color='#800080', label=price1)
    ax1.plot(dist_df['Year'], dist_df[price2], marker='o', linestyle='-', color='#BA55D3', label=price2)
    ax1.set_title('Harvest Price over time for Crop Combination 1')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Harvest Price (Rs per Quintal)')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(dist_df['Year'], dist_df[price3], marker='o', linestyle='-', color='#333333', label=price3)
    ax2.plot(dist_df['Year'], dist_df[price4], marker='o', linestyle='-', color='#808080', label=price4)
    ax2.set_title('Harvest Price over time for Crop Combination 2')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Harvest Price (Rs per Quintal)')
    ax2.grid(True)
    ax2.legend()

    plt.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.1)
    st.pyplot(fig)


if selected_district == 'Please select':
    pass
else:
  yield_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2)
  price_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2)



import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('D://MarketDrivenCropPlanning//data-analytics//dataset//Cleaned_dataset.csv')
access_df = pd.read_csv('D://MarketDrivenCropPlanning//data-analytics//dataset//render1.csv')  # Assuming your access data CSV is named 'access.csv'

def get_crop_combinations(selected_district):
    global combo1crop1, combo1crop2, combo2crop1, combo2crop2
    if selected_district == 'Please select':
        pass
    else:
        combo1crop1 = access_df.loc[access_df["District"] == selected_district, "Combination_1_Crop_1"].values[0]
        combo1crop2 = access_df.loc[access_df["District"] == selected_district, "Combination_1_Crop_2"].values[0]
        combo2crop1 = access_df.loc[access_df["District"] == selected_district, "Combination_2_Crop_1"].values[0]
        combo2crop2 = access_df.loc[access_df["District"] == selected_district, "Combination_2_Crop_2"].values[0]
        st.write("Here are the 2 best combinations for your district!")
        st.write("*Crop Comination 1:",f"{combo1crop1.capitalize()} & {combo1crop2.capitalize()}*")
        st.write("*Crop Comination 2:",f"{combo2crop1.capitalize()} & {combo2crop2.capitalize()}*")

def yield_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2, selected_district):
    if selected_district == 'Please select':
        pass
    else:
        dist_df = df[df['Dist Name'] == selected_district]
        yield1 = combo1crop1 + ' YIELD (Kg per ha)'
        yield2 = combo1crop2 + ' YIELD (Kg per ha)'
        yield3 = combo2crop1 + ' YIELD (Kg per ha)'
        yield4 = combo2crop2 + ' YIELD (Kg per ha)'

        fig = make_subplots(rows=1, cols=2, subplot_titles=('Yield over time for Crop Combination 1', 'Yield over time for Crop Combination 2'), horizontal_spacing=0.2)

        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[yield1], mode='lines+markers', name=yield1), row=1, col=1)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[yield2], mode='lines+markers', name=yield2), row=1, col=1)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[yield3], mode='lines+markers', name=yield3), row=1, col=2)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[yield4], mode='lines+markers', name=yield4), row=1, col=2)

        fig.update_layout(title='Yield over time',
                          xaxis_title='Year',
                          yaxis_title='Yield (Kg per ha)',
                          width=800,
                          height=300,
                          margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig, use_container_width=True)

def price_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2, selected_district):
    if selected_district == 'Please select':
        pass
    else:
        dist_df = df[df['Dist Name'] == selected_district]
        price1 = combo1crop1 + ' HARVEST PRICE (Rs per Quintal)'
        price2 = combo1crop2 + ' HARVEST PRICE (Rs per Quintal)'
        price3 = combo2crop1 + ' HARVEST PRICE (Rs per Quintal)'
        price4 = combo2crop2 + ' HARVEST PRICE (Rs per Quintal)'

        fig = make_subplots(rows=1, cols=2, subplot_titles=('Harvest Price over time for Crop Combination 1', 'Harvest Price over time for Crop Combination 2'), horizontal_spacing=0.2)

        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[price1], mode='lines+markers', name=price1), row=1, col=1)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[price2], mode='lines+markers', name=price2), row=1, col=1)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[price3], mode='lines+markers', name=price3), row=1, col=2)
        fig.add_trace(go.Scatter(x=dist_df['Year'], y=dist_df[price4], mode='lines+markers', name=price4), row=1, col=2)

        fig.update_layout(title='Harvest Price over time',
                          xaxis_title='Year',
                          yaxis_title='Harvest Price (Rs per Quintal)',
                          width=800,
                          height=300,
                          margin=dict(l=50, r=50, t=50, b=50))
        st.plotly_chart(fig, use_container_width=True)

def main():
    st.set_page_config(layout="wide")  # Set the page layout to wide
    st.title("Effective Crop Combinations")
    district_options = list(df['Dist Name'].unique())
    selected_district = st.selectbox("Select District:", ['Please select']+district_options, key="select_district")

    if selected_district != 'Please select':
        get_crop_combinations(selected_district)
        yield_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2, selected_district)
        price_plots(combo1crop1, combo1crop2, combo2crop1, combo2crop2, selected_district)

if __name__ == "__main__":
    main()
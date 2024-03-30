import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def process_data(df):
    years = df['Year'].to_list()
    rice_yield = df['Rice Yield ( in tonn per ha )'].to_list()
    wheat_yield = df['Wheat Yield ( in tonn per ha  )'].to_list()
    rice_price = df['Rice Price (in RS per quintal )'].to_list()
    wheat_price = df['Wheat Price(in RS per quintal )'].to_list()

    fig_yield = go.Figure()
    fig_yield.add_trace(go.Scatter(x=years, y=rice_yield, mode='lines+markers', name='Rice Yield'))
    fig_yield.add_trace(go.Scatter(x=years, y=wheat_yield, mode='lines+markers', name='Wheat Yield'))
    fig_yield.update_layout(title='Yield Trend Over The Years',
                            xaxis_title='Year',
                            yaxis_title='Yield (tonnes per hectare)')

    fig_price = go.Figure()
    fig_price.add_trace(go.Scatter(x=years, y=rice_price, mode='lines+markers', name='Rice Price'))
    fig_price.add_trace(go.Scatter(x=years, y=wheat_price, mode='lines+markers', name='Wheat Price'))
    fig_price.update_layout(title='Price Trend Over The Years',
                            xaxis_title='Year',
                            yaxis_title='Price (Rs per quintal)')

    return fig_yield, fig_price

def main():
    st.title("Welcome to the farmer dashboard!")

    # Create an upload file button
    uploaded_file = st.file_uploader("Upload csv file containing farm data:", type=['csv'])

    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.write("Uploaded CSV file:")
        st.write(df)

        # Create a process button
        if st.button("Process"):
            # Process the data
            fig_yield, fig_price = process_data(df)

            # Display the graphs
            st.plotly_chart(fig_yield, use_container_width=True)
            st.plotly_chart(fig_price, use_container_width=True)

if __name__ == "__main__":
    main()
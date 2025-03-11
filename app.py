from utils.fetch_data import fetch_stock_data
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


plt.switch_backend('Agg') 


# # list of tuples containing company symbols and names.
stocks = [
    ("AAPL", "Apple Inc."),
    ("MSFT", "Microsoft Corp."),
    ("GOOGL", "Alphabet Inc (Google)"),
    ("GOOG", "Alphabet Inc (Google) - Class C"),
    ("AMZN", "Amazon.com Inc"),
    ("NVDA", "NVIDIA Corporation"),
    ("META", "Meta Platforms Inc(Facebook)"),
    ("TSLA", "Tesla Inc"),
    ("TSM", "Taiwan Semiconductor Manufacturing Company (TSMC)"),
    ("BRK-B", "Berkshire Hathaway Inc. - Class B"),
    ("ADBE", "Adobe Inc."),
    ("INTC", "Intel Corporation"),
    ("ASML", "ASML Holding"),
    ("ORCL", "Oracle Corporation"),
    ("CRM", "Salesforce Inc."),
    ("AMD", "Advanced Micro Devices"),
    ("QCOM", "Qualcomm Incorporated"),
    ("PYPL", "PayPal Holdings Inc."),
    ("SPOT", "Spotify Technology S.A."),
    ("ZM", "Zoom Video Communications"),
    ("NOW", "ServiceNow Inc.")
]

st.title('Stock Price Trend Visualization')

# Dropdown for selecting a stock symbol
stock_company = st.selectbox('Select a company', [stock[1] for stock in stocks])  # Add your stock symbols here






# Fetch the data based on the selected stock symbol
if stock_company:
    df = fetch_stock_data(stock_company)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.index = pd.to_datetime(df.index) 
    df = df.rename(columns={'daily_return': 'Daily Return (%)'})
    df.set_index('date', inplace=True)
  
    
   


    # Display the raw data (optional)
    st.subheader('Raw Data')
    st.write(df)

    # Plotting the data
    st.subheader(f'{stock_company} Price Trend')

    # Check if the DataFrame has data
if not df.empty:


    # Create a plot with matplotlib and seaborn
    plt.figure(figsize=(25, 18))


    
    

    # Add title and labels
    plt.title(f'{stock_company} Stock Price Over Time', fontsize=30)
    plt.xlabel('Date', fontsize=30)
    plt.ylabel('Price (USD)', fontsize=30)

    button_placeholder = st.empty()


    # Initially, show the button
    volume_button = button_placeholder.button("Show Volume Chart")
    

    if volume_button:
        weekly_volume = df['volume'].resample('W').sum().reset_index()
        weekly_volume['date'] = pd.to_datetime(weekly_volume['date'], errors='coerce')
        plt.bar(weekly_volume["date"], weekly_volume["volume"], color="blue",width=5)
        plt.title(f'{stock_company} Stock Volume.', fontsize=25)
        plt.ylabel("Total Weekly Trading Volume", fontsize=30)
        show_price = st.button("Show Price Chart")
        button_placeholder.empty() 
    
    else:
        sns.lineplot(x='date', y='close', data=df, label='Closing Price', color='blue')
         # sns.lineplot(x='date', y='close', data=df, label='Close Price', color='red')
        sns.lineplot(x="date", y="sma_200", data=df,label="SMA_200", color="black", linestyle='--'  )
        plt.legend(fontsize=25) 


    
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # This will show 'Jan 2025', 'Feb 2025', etc.
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # This will set the x-axis tick marks to months
    plt.gca().tick_params(axis='x', labelsize=25) 
    plt.gca().tick_params(axis='y', labelsize=25) 

    # Display the plot in the Streamlit app
    st.pyplot(plt)

else:
    st.write(f"No data available for {stock_company}")
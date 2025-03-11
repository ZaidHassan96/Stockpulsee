import pandas as pd
from sqlalchemy import text
from db.db_config import engine








def fetch_stock_data(company):
    try:

        with engine.connect() as connection:
            # Use parameterized query to prevent SQL injection
            query = text("SELECT close, open, date, daily_return, volatility, sma_200, volume FROM stock_data WHERE company = :company")
            
            # Execute query with parameters and fetch results
            result = connection.execute(query, {"company": company})
            
            # Convert result to DataFrame
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            
            return df
            
    except Exception as error:
        print(f"Error: {error}")
        return pd.DataFrame()  # Return empty DataFrame on error
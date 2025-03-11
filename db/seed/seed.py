import csv
from pathlib import Path
import streamlit as st
from sqlalchemy import create_engine, text
import traceback  # Add this for better error reporting
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db_config import engine


def seed_database():
    try:
      
        
        with engine.connect() as connection:
            # Drop and create table (your existing code)
            connection.execute(text("DROP TABLE IF EXISTS stock_data;"))
            connection.commit()
            
            # Create table query (your existing code)
            create_table_query = text('''
            CREATE TABLE IF NOT EXISTS stock_data (
                date VARCHAR(100),
                close FLOAT,
                high FLOAT,
                low FLOAT,
                open FLOAT,
                volume BIGINT,
                company VARCHAR(100),
                daily_return VARCHAR(20),
                sma_200 FLOAT,
                volatility FLOAT
            );
            ''')
            connection.execute(create_table_query)
            connection.commit()
            
            print("Table 'stock_data' created successfully")
            
            # Read CSV data
            path = Path(__file__).resolve().parent.parent / 'data/stocks.csv'
            print(f"Reading CSV file from: {path}")
            lines = path.read_text().splitlines()
            print(f"Read {len(lines)} lines from CSV")
            
            reader = csv.reader(lines)
            header_row = next(reader)  # Skip header row
            
            # Add a counter to track progress
            row_count = 0
            
            # Process and insert data in smaller batches
            for line in reader:
                try:
                    # Clean up the data
                    if len(line) == 11:  # Handle the case where "Inc" is separated
                        line.pop(7)
                    
                    # Replace empty values with None and remove quotes
                    cleaned_line = [item.replace('"', '') if item and item != '' else None for item in line]
                    
                    # Insert data
                    insert_query = text('''
                    INSERT INTO stock_data 
                    (date, close, high, low, open, volume, company, daily_return, sma_200, volatility) 
                    VALUES (:date, :close, :high, :low, :open, :volume, :company, :daily_return, :sma_200, :volatility)
                    ''')
                    
                    connection.execute(insert_query, {
                        "date": cleaned_line[0],
                        "close": cleaned_line[1],
                        "high": cleaned_line[2],
                        "low": cleaned_line[3],
                        "open": cleaned_line[4],
                        "volume": cleaned_line[5],
                        "company": cleaned_line[6],
                        "daily_return": cleaned_line[7],
                        "sma_200": cleaned_line[8],
                        "volatility": cleaned_line[9] if len(cleaned_line) > 9 else None
                    })
                    
                    row_count += 1
                    
                    # Print progress every 100 rows
                    if row_count % 100 == 0:
                        print(f"Processed {row_count} rows")
                        connection.commit()  # Commit in batches
                        
                except Exception as e:
                    print(f"Error processing row: {line}")
                    print(f"Error details: {str(e)}")
                    # Continue with next row instead of failing completely
                    continue
            
            # Final commit
            connection.commit()
            print(f"Data insertion complete. Inserted {row_count} rows successfully.")
            
        return "Database seeded successfully!"
        
    except Exception as error:
        print(f"Error: {error}")
        traceback.print_exc()  # Print the full traceback
        return f"Error seeding database: {error}"

if __name__ == "__main__":
    result = seed_database()
    print(result)
#!/bin/bash

# Step 1: Download stock data using download_Data.py
echo "Downloading stock data..."
python3 download_Data.py

# Step 2: Seed the database with stock data
echo "Seeding the database..."
python3 seed_database.py

echo "Process completed successfully!"

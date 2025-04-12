import streamlit as st
from sqlalchemy import create_engine




production = False

if production:

    host = st.secrets["connections"]["production"]["host"]
    database = st.secrets["connections"]["production"]["database"]
    username = st.secrets["connections"]["production"]["username"]
    password = st.secrets["connections"]["production"]["password"]
    port = st.secrets["connections"]["production"]["port"]

else:
    host = st.secrets["connections"]["development"]["host"]
    database = st.secrets["connections"]["development"]["database"]
    username = st.secrets["connections"]["development"]["username"]
    password = st.secrets["connections"]["development"]["password"]
    port = st.secrets["connections"]["development"]["port"]




        
            
try:
     #Create SQLAlchemy engine
     engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
     print(engine)
        # connection = st.connection("postgresql")
     print("Database connection successful!")

except Exception as error:
        print(f"Error: {error}")
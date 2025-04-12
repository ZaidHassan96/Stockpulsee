## Stockpulsee

**Stockpulsee** allows users to view the top 21 tech stocks through an interactive visual display and raw data table. The application showcases key stock metrics, including:

- **Volume**
- **Company**
- **Daily Return**
- **SMA_200** (200-day Simple Moving Average)
- **Volatility**
- **Open**
- **Close**

With this, users can track trends and analyze stock performance over time with both graphical charts and detailed data tables.


### Powered by:

- **Python**
- **SQLAlchemy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **yFinance**
- **Streamlit**



### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ZaidHassan96/Stockpulsee.git
   cd Stockpulsee```
   
2. Install dependencies:
```bash
   pip install -r requirements.txt
```

### Set up the PostgreSQL Database

You’ll need to configure your PostgreSQL database connection. This project uses SQLAlchemy to connect to the database.

1. Create the `secrets.toml` file in the root directory of the project.

2. Add the following configuration to `secrets.toml` to configure your database connection:

   ```toml
   [connections.development]
   type = "sql"
   dialect = "postgresql"
   host = "localhost"
   port = "5432"
   database = "companies"
   username = "your_username"
   password = "your_password"


### Running the Application

To automate the entire process (downloading stock data and seeding the database), you can run the provided `automate.sh` script.

1. Make the script executable:

   ```bash
   chmod +x automate.sh
   ```

2. Run the script:
     ```bash
     ./automate.sh
     ```


### Running the Streamlit App

After the database has been seeded, you can visualize the stock price trends with Streamlit.

Run the Streamlit app with the following command:

```bash
streamlit run app.py
```
   

#What was the change in price of the stock overtime?

import matplotlib
import pip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime

sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv(".\\Asset\\portfolio_data.csv")
print(df)

tech_list = ["AAPL", "GOOG", "MSFT", "AMZN"]
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

#Download stock data
for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)

company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]

df = pd.concat(company_list, axis=0)
df.tail(10)

print(df)

#Descriptive Statistics about the Data

AAPL.describe()
print(AAPL.describe())

#Information About the Data

AAPL.info()
print(AAPL.info())

# let's see the historical view of the closing price

plt.figure(figsize=(15, 10))
plt.subplots_adjust(top= 1.25, bottom= 1.2)

for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
    company["Adj Close"].plot()
    plt.ylabel("Adj Close")
    plt.xlabel(None)
    plt.title(f"Closing Price of {tech_list[i-1]}")

plt.tight_layout()
plt.show()

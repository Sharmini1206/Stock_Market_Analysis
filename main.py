#What was the change in price of the stock overtime?

import matplotlib
import pdr as pdr
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

#now let's plot the total volume of stock being traded each day
plt.figure(figsize=(15, 10))
plt.subplots_adjust(top= 1.25, bottom= 1.2)

for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
    company["Volume"].plot()
    plt.ylabel("Volume")
    plt.xlabel(None)
    plt.title(f"Sales volume of {tech_list[i-1]}")

plt.tight_layout()
plt.show()

#What was the moving average(MA) of the various stocks?

ma_day = [10, 20, 50]

for ma in ma_day:
    for company in company_list:
        column_name = f"MA for {ma} days"
        company[column_name] = company["Adj Close"].rolling(ma).mean()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.subplots_adjust(top=1.25, bottom=1.2)
fig.set_figheight(10)
fig.set_figwidth(15)

AAPL[["Adj Close", "MA for 10 days", "MA for 20 days",
          "MA for 50 days"]].plot(ax=axes[0, 0])
axes[0, 0].set_title("APPLE")

GOOG[["Adj Close", "MA for 10 days", "MA for 20 days",
          "MA for 50 days"]].plot(ax=axes[0, 1])
axes[0, 1].set_title("GOOGLE")

MSFT[["Adj Close", "MA for 10 days", "MA for 20 days",
          "MA for 50 days"]].plot(ax=axes[1, 0])
axes[1, 0].set_title("MICROSOFT")

AMZN[["Adj Close", "MA for 10 days", "MA for 20 days",
          "MA for 50 days"]].plot(ax=axes[1, 1])
axes[1, 1].set_title("AMAZON")

fig.tight_layout()
plt.show()

# What was the daily return of stock on average

#We'll use pct_change to find the percent change for each day
for company in company_list:
    company["Daily Return"] = company["Adj Close"].pct_change()

#Then we'll plot the daily return percentage
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(15)

AAPL["Daily Return"].plot(ax=axes[0, 0], legend=True,
                          linestyle="--", marker="o")
axes[0, 0].set_title("APPLE")

GOOG["Daily Return"].plot(ax=axes[0, 1], legend=True,
                          linestyle="--", marker="o")
axes[0, 1].set_title("GOOGLE")

MSFT["Daily Return"].plot(ax=axes[1, 0], legend=True,
                          linestyle="--", marker="o")
axes[1, 0].set_title("MICROSOFT")

AMZN["Daily Return"].plot(ax=axes[1, 1], legend=True,
                          linestyle="--", marker="o")
axes[1, 1].set_title("AMAZON")

fig.tight_layout()
plt.show()

#now let's get an overall look
# at the average daily return using a histogram.
plt.figure(figsize=(12, 9))

for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
    company["Daily Return"].hist(bins=50)
    plt.xlabel("Daily Return")
    plt.ylabel("Counts")
    plt.title(f"{column_name[i -1]}")

plt.tight_layout
plt.show()

#What was the correlation between
# different stocks closing prices

#Grab all the closing prrices for
# the techstock list into one dataFrame

closing_df = yf.download(tech_list, start=start,
                         end=end)["Adj Close"]

#Make a new tech returns DataFrame
tech_rets = closing_df.pct_change()
tech_rets.head()

print(tech_rets.head())

#Comparing Google to itself show
# a perfetly linear relationship

sns.jointplot(x="GOOG", y="GOOG", data=tech_rets,
              kind="scatter", color="seagreen")
plt.show()

#We'll use joinplot to compare the daily returns
# of Google and Microsoft

sns.jointplot(x="GOOG", y="MSFT", data=tech_rets,
              kind="scatter", color="seagreen")
plt.show()

#We can simply pairplot on our DataFrame for
# an automtic visual analysis of all the comparisons

sns.pairplot(tech_rets, kind="reg")
plt.show()

#set up our figure by naming it returns_fig, call pairplot on the DaataFrame
returns_fig = sns.PairGrid(tech_rets.dropna())
plt.show()


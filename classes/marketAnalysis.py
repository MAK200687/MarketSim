
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class MarketAnalysis:
    def __init__(self):
        self.data = pd.read_csv("data/marketsim_stocks.csv")
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        os.makedirs("charts", exist_ok=True)

    def displayData(self):
        print(self.data.head())

    def filterStock(self, symbol):
        result = self.data[self.data["Symbol"] == symbol]
        return result

    def getLatestPrice(self, symbol):
        stockData = self.filterStock(symbol)

        if stockData.empty:
            return None

        latestPrice = stockData.sort_values("Date").iloc[-1]["Close"]
        return latestPrice

    def calculateReturns(self, symbol):
        stockData = self.filterStock(symbol).copy()
        stockData = stockData.sort_values("Date")
        stockData["Return"] = stockData["Close"].pct_change() * 100
        return stockData

    def displaySummary(self):
        print(self.data.describe())

    def calculateAverageReturn(self, symbol):
        stockData = self.calculateReturns(symbol)
        returns = stockData["Return"].dropna()

        if returns.empty:
            return 0

        return np.mean(returns)

    def calculateVolatility(self, symbol):
        stockData = self.calculateReturns(symbol)
        returns = stockData["Return"].dropna()

        if len(returns) < 2:
            return 0

        return np.std(returns)

    def calculatePortfolioValue(self, portfolio):
        totalValue = 0

        for symbol, quantity in portfolio.holdings.items():
            price = self.getLatestPrice(symbol)

            if price is not None:
                totalValue += price * quantity

        return totalValue

    def calculateRiskReturn(self, symbol):
        averageReturn = self.calculateAverageReturn(symbol)
        volatility = self.calculateVolatility(symbol)

        return averageReturn, volatility

    def plotStockPrice(self, symbol):
        stockData = self.filterStock(symbol).sort_values("Date")

        if stockData.empty:
            print("Stock not found")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(stockData["Date"], stockData["Close"], marker="o")
        plt.title(symbol + " Historical Stock Prices")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (PKR)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("charts/" + symbol + "_price.png")
        plt.show()
        plt.close()

    def plotPortfolioValue(self, portfolio):
        totalValue = 0

        for symbol, quantity in portfolio.holdings.items():
            price = self.getLatestPrice(symbol)

            if price is not None:
                totalValue += price * quantity

        plt.figure(figsize=(7, 5))
        plt.bar(["Portfolio"], [totalValue])
        plt.title("Current Portfolio Value")
        plt.ylabel("Value (PKR)")
        plt.tight_layout()
        plt.savefig("charts/portfolio_value.png")
        plt.show()
        plt.close()

    def plotStockReturns(self):
        returnData = self.data.copy()
        returnData = returnData.sort_values("Date")
        returnData["Return"] = returnData.groupby("Symbol")["Close"].pct_change() * 100
        returnData = returnData.dropna()

        if returnData.empty:
            print("Not enough data for returns")
            return

        plt.figure(figsize=(10, 5))
        sns.boxplot(data=returnData, x="Symbol", y="Return")
        plt.title("Stock Returns Comparison")
        plt.tight_layout()
        plt.savefig("charts/stock_returns.png")
        plt.show()
        plt.close()

    def plotVolatility(self):
        volatilityData = []

        for symbol in self.data["Symbol"].unique():
            volatility = self.calculateVolatility(symbol)
            volatilityData.append({
                "Symbol": symbol,
                "Volatility": volatility
            })

        volatilityFrame = pd.DataFrame(volatilityData)

        plt.figure(figsize=(10, 5))
        sns.barplot(data=volatilityFrame, x="Symbol", y="Volatility")
        plt.title("Stock Volatility Comparison")
        plt.ylabel("Standard Deviation of Returns (%)")
        plt.tight_layout()
        plt.savefig("charts/volatility.png")
        plt.show()
        plt.close()

    def plotCorrelation(self):
        priceData = self.data.pivot(
            index="Date",
            columns="Symbol",
            values="Close"
        )

        returnData = priceData.pct_change() * 100
        correlation = returnData.corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Stock Return Correlation")
        plt.tight_layout()
        plt.savefig("charts/correlation.png")
        plt.show()
        plt.close()

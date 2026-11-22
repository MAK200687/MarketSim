
from classes.marketAnalysis import MarketAnalysis
from classes.portfolio import Portfolio

analysis = MarketAnalysis()
portfolio = Portfolio()

print("TEST 1: Stock Price Chart")
analysis.plotStockPrice("ABC")

print("TEST 2: Portfolio Value Chart")
analysis.plotPortfolioValue(portfolio)

print("TEST 3: Stock Returns Comparison")
analysis.plotStockReturns()

print("TEST 4: Stock Volatility")
analysis.plotVolatility()

print("TEST 5: Stock Correlation")
analysis.plotCorrelation()

print("\nALL CHARTS COMPLETED")

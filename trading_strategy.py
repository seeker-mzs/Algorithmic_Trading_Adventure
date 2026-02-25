import yfinance as yf
import pandas as pd
import numpy as np

class TradingStrategy:
    def __init__(self, symbol, start_date, end_date, capital=5000):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.capital = capital

        
        self.data = None
        self.trades = pd.DataFrame(columns=['Type','Shares','Price','Profit'])
    
    
    def download_and_clean(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        
        
        if isinstance(self.data.columns, pd.MultiIndex):
            self.data.columns = self.data.columns.droplevel(1)
        
        
        self.data = self.data.drop_duplicates().ffill()
        self.data = self.data.astype('float32') 
    
    
    def calculate_indicators(self, ma_short=50, ma_long=200):
        self.data['MA_short'] = self.data['Close'].rolling(window=ma_short).mean()
        self.data['MA_long'] = self.data['Close'].rolling(window=ma_long).mean()
    
    
    def generate_signals(self):
       
        ma_s_prev = self.data['MA_short'].shift(1)
        ma_l_prev = self.data['MA_long'].shift(1)
        
       
        self.data['Buy'] = ((self.data['MA_short'] > self.data['MA_long']) & 
                            (ma_s_prev <= ma_l_prev))
        
        self.data['Sell'] = ((self.data['MA_short'] < self.data['MA_long']) & 
                             (ma_s_prev >= ma_l_prev))
    
    
    def run_strategy(self):
        position = 0
        shares = 0
        capital = self.capital

        close_prices = self.data['Close'].to_numpy()
        buy_signals = self.data['Buy'].to_numpy()
        sell_signals = self.data['Sell'].to_numpy()
        
        for i in range(len(self.data)):
            price = close_prices[i]
            
            if buy_signals[i] and position == 0:
                shares = int(capital // price)
                position = 1
                capital -= shares * price
                self.trades.loc[len(self.trades)] = ['BUY', shares, price, 0.0]
            
            elif sell_signals[i] and position == 1:
                profit = (price - self.trades.iloc[-1]['Price']) * shares
                capital += shares * price
                self.trades.loc[len(self.trades)] = ['SELL', shares, price, profit]
                position = 0
                shares = 0
        
        if position == 1:
            profit = (close_prices[-1] - self.trades.iloc[-1]['Price']) * shares
            capital += shares * close_prices[-1]
            self.trades.loc[len(self.trades)] = ['SELL', shares, close_prices[-1], profit]
        
        self.capital = capital
    
    def evaluate(self):
        print("------ TRADES EXECUTED ------")
        print(self.trades)
        print("-----------------------------")
        print(f"Final Capital: ${self.capital:.2f}")

    


if __name__ == "__main__":
    if __name__ == "__main__":
        symbol = input("Enter stock symbol (e.g., AAPL): ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        capital = 5000

        strategy = TradingStrategy(symbol, start_date, end_date, capital)
    

        strategy.download_and_clean()
        strategy.calculate_indicators()
        strategy.generate_signals()
        strategy.run_strategy()
        strategy.evaluate()
    
    
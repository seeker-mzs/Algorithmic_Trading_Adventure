# Algorithmic Trading Adventure

A Python-based trading simulator using the Golden Cross / Death Cross strategy.  
Enter a stock symbol and date range to see executed trades, profits, and a trading plot.



## Requirements

- Python 3.8+
- Install libraries:

```bash
pip install yfinance pandas numpy matplotlib
````

---

## How to Run

1. Open terminal and go to project folder:

```bash
cd F:\Task1AlgorithmicTradingAdventure
```

2. Run the script:

```bash
python trading_strategy.py
```

3. Enter:

* Stock symbol (e.g., `AAPL`, `TSLA`)
* Start date (`YYYY-MM-DD`)
* End date (`YYYY-MM-DD`)

> Initial capital is fixed at $5000.

4. See output:

* Trades executed
* Final capital
* Price plot with buy/sell points

---

## Notes

* More volatile stocks like `TSLA`, `AMC`, or `GME` give more frequent trades.
* MA50 & MA200 are default; change in code to adjust trade frequency.

```

---
```

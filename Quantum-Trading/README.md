# Quantum Trading System

This project contains a quantum trading system using a momentum and mean reversion strategy on ETFs. The system reads data from a CSV file, processes it to identify buy/sell signals, and calculates the potential profit/loss. The results are displayed in a simple GUI and can be saved for further analysis.

## Contents
- **quantum_trading_system.py**: Main script with GUI for running the trading system.
- **etf_data.csv**: Sample ETF data file with fictitious data for testing.

## How to Use
1. **Load Data**: Click the "Load CSV Data" button and select the `etf_data.csv` file.
2. **Process Data**: The script will analyze the data and display the results in the GUI.
3. **Save Results**: Click "Save Results" to save the output to a text file.

## Requirements
- Python 3.x
- Pandas
- Numpy
- Tkinter (for the GUI)

## Trading Strategy
- **Momentum and Mean Reversion**: The system looks for ETFs that have shown strong momentum but are temporarily pulling back, anticipating a reversion to the mean.

## Example Output
2024-08-01 | SPY | Signal: Buy | Profit/Loss: 3.00 2024-08-02 | QQQ | Signal: Sell | Profit/Loss: -1.50

Total Cumulative Profit: $1.50


This quantum trading system is a demonstration of a simple yet effective trading strategy that 

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# Load CSV data
def load_data():
    file_path = filedialog.askopenfilename()
    if file_path:
        df = pd.read_csv(file_path)
        process_data(df)
    else:
        messagebox.showwarning("File not selected", "Please select a CSV file.")

# Process data and apply trading strategy
def process_data(df):
    # Apply the Momentum and Mean Reversion strategy
    df['Signal'] = np.where((df['Close'] > df['20D_MA']) & (df['RSI'] < 70) & (df['Close'] < df['50D_MA']), 'Buy', 'Hold')
    df['Signal'] = np.where((df['Close'] < df['20D_MA']) & (df['RSI'] > 30), 'Sell', df['Signal'])
    
    df['Profit/Loss'] = np.where(df['Signal'] == 'Buy', df['Close'].shift(-1) - df['Close'], 0)
    df['Profit/Loss'] = np.where(df['Signal'] == 'Sell', df['Close'] - df['Close'].shift(-1), df['Profit/Loss'])
    
    df['Cumulative_Profit'] = df['Profit/Loss'].cumsum()

    display_results(df)

# Display the results in the GUI
def display_results(df):
    results_text.delete(1.0, tk.END)
    for index, row in df.iterrows():
        results_text.insert(tk.END, f"{row['Date']} | {row['ETF']} | Signal: {row['Signal']} | Profit/Loss: {row['Profit/Loss']:.2f}\n")
    
    total_profit = df['Cumulative_Profit'].iloc[-1]
    results_text.insert(tk.END, f"\nTotal Cumulative Profit: ${total_profit:.2f}")
    
    save_button.config(state=tk.NORMAL)

# Save the output to a text file
def save_output():
    output = results_text.get(1.0, tk.END)
    with open("trading_results.txt", "w") as file:
        file.write(output)
    messagebox.showinfo("Saved", "Results saved successfully!")

# Setting up the GUI
app = tk.Tk()
app.title("Quantum Trading System")

load_button = tk.Button(app, text="Load CSV Data", command=load_data)
load_button.pack(pady=10)

results_text = tk.Text(app, height=20, width=80)
results_text.pack(pady=10)

save_button = tk.Button(app, text="Save Results", command=save_output, state=tk.DISABLED)
save_button.pack(pady=10)

app.mainloop()

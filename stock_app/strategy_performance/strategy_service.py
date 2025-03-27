import pandas as pd

def load_data(file_path):
    
    df = pd.read_excel(file_path)
    df['datetime'] = pd.to_datetime(df['datetime'])  # Ensure datetime format
    df.set_index('datetime', inplace=True)  # Set datetime as index
    return df

def calculate_moving_average(data, window):
    return data['close'].rolling(window=window).mean()

def generate_signals(data):
    
    data['short_ma'] = calculate_moving_average(data, 7) 
    # Define long-term moving averages
    periods = {
        '1_month': 30,
        '3_month': 90,
        '6_month': 180,
        '1_year': 365
    }

    results = {}

    for label, window in periods.items():
        data[f'long_ma_{label}'] = calculate_moving_average(data, window)
        data[f'signal_{label}'] = 0  # Default signal

        # Generate buy/sell signals
        prev_short_ma = data['short_ma'].shift(1)
        prev_long_ma = data[f'long_ma_{label}'].shift(1)

        data.loc[(data['short_ma'] > data[f'long_ma_{label}']) & (prev_short_ma <= prev_long_ma), f'signal_{label}'] = 1  # Buy
        data.loc[(data['short_ma'] < data[f'long_ma_{label}']) & (prev_short_ma >= prev_long_ma), f'signal_{label}'] = -1  # Sell

        results[label] = backtest_strategy(data, f'signal_{label}')

    return results

def backtest_strategy(data, signal_column, initial_balance=10000):
    balance = initial_balance
    position = 0
    buy_price = 0

    for i in range(len(data)):
        signal = data[signal_column].iloc[i]
        close_price = data['close'].iloc[i]

        if signal == 1:  # Buy
            position = balance / close_price
            buy_price = close_price
            balance = 0

        elif signal == -1 and position > 0:  # Sell
            balance = position * close_price
            position = 0

    final_balance = balance + (position * data['close'].iloc[-1])
    return {
        "initial_balance": initial_balance,
        "final_balance": round(final_balance, 2),
        "return_percentage": round(((final_balance - initial_balance) / initial_balance) * 100, 2)
    }

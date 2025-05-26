import pandas as pd
import numpy as np

def calculate_rsi(close, window=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def generate_signal_strength(df):
    df['10 MA'] = df['Close'].rolling(10).mean()
    df['50 MA'] = df['Close'].rolling(50).mean()
    df['RSI'] = calculate_rsi(df['Close'], window=14)
    df['Volume Spike'] = df['Volume'] > df['Volume'].rolling(20).mean()

    df['Signal Score'] = 0
    df.loc[df['10 MA'] > df['50 MA'], 'Signal Score'] += 1
    df.loc[df['RSI'] < 30, 'Signal Score'] += 1
    df.loc[df['Volume Spike'], 'Signal Score'] += 1

    return df

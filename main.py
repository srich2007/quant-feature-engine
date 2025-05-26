import argparse
import pandas as pd
import yfinance as yf
from signal_generator import generate_signal_strength

def get_data(ticker):
    df = yf.download(ticker, period='1y', interval='1d')
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quant Feature Generator")
    parser.add_argument('--ticker', type=str, required=True, help='Ticker symbol (e.g. AAPL)')
    parser.add_argument('--export', type=str, default=None, help='Optional: path to export CSV')

    args = parser.parse_args()

    df = get_data(args.ticker.upper())
    df = generate_signal_strength(df)

    print(df[['Close', '10 MA', '50 MA', 'RSI', 'Volume Spike', 'Signal Score']].tail())

    if args.export:
        df.to_csv(args.export, index=True)
        print(f"CSV exported to {args.export}")

# quant-feature-engine
A signal generator that uses raw OHLCV data to generate alpha. Combines RSI, moving average crossover, and volume-based indicators with a composite signal scoring system. Built for integration into strategy testing and ML-based signal research pipelines.

## Features

- ✅ RSI (Relative Strength Index)
- ✅ 10 vs 50 day Moving Average Crossover
- ✅ Volume Spike Signal (based on 20-day avg)
- ✅ Composite Signal Score

## Example

| Date       | Close | RSI | 10 MA | 50 MA | Volume Spike | Signal Score |
|------------|-------|-----|--------|--------|---------------|----------------|
| 2024-01-15 | 312.4 | 25  | 308.2 | 301.7  | True          | 3              |

## Usage

```bash
python main.py
# Or import directly:
from signal_generator import generate_signal_strength

Dependencies
import pandas as pd
import numpy as np
import yfinance as yf

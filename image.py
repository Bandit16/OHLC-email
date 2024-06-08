
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import mplfinance as mpf
import ta

# Load the sample stock data
def img():
    with pd.ExcelFile('data.xlsx') as xlsx:
        data = pd.read_excel(xlsx, sheet_name='Sheet2', thousands=',')
    df = pd.DataFrame(data)

    # Convert date column to datetime and set as index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Calculate RSI
    df['RSI'] = ta.momentum.rsi(df['close'], window=14)

    # Calculate MACD
    macd = ta.trend.MACD(df['close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['MACD_hist'] = macd.macd_diff()

    # Create additional plots for RSI and MACD
    rsi_plot = mpf.make_addplot(df['RSI'], panel=1, color='r', secondary_y=False, title='RSI')
    macd_line_plot = mpf.make_addplot(df['MACD'], panel=2, color='b', secondary_y=False)
    macd_signal_plot = mpf.make_addplot(df['MACD_signal'], panel=2, color='r', secondary_y=False)
    macd_hist_plot = mpf.make_addplot(df['MACD_hist'], panel=2, type='bar', color='gray', secondary_y=False, alpha=0.5)

    # Plot candlestick chart with additional indicators
    mpf.plot(df, 
            type='candle', 
            style='binance', 
            title='Stock Price Data', 
            volume=False, 
            addplot=[rsi_plot, macd_line_plot, macd_signal_plot, macd_hist_plot],
            panel_ratios=(3, 1, 1),
            savefig='stock_chart.png',
            
            )
    
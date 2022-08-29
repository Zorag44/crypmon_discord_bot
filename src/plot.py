from datetime import datetime, timedelta
import pandas as pd
import os
import pandas_datareader as pdr
import plotly.graph_objects as go
# from pathlib import Path
# import plotly.io as pio
# pio.kaleido.scope.mathjax = None

# f = Path.cwd().joinpath("images1")

# if not f.is_dir(): f.mkdir()

# f = f.joinpath("fig1.png")

if not os.path.isdir('images'):
    os.mkdir('images')
def data(cryptocurrency):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    last_year_date = (now - timedelta(days=365)).strftime("%Y-%m-%d")

    start = pd.to_datetime(last_year_date)
    end = pd.to_datetime(current_date)

    data = pdr.get_data_yahoo(f"{cryptocurrency}-USD", start, end)

    return data

# print(data('BTC'))
# import plotly
# import kaleido

# print(plotly.__version__, kaleido.__version__)
def Plot(sym):
    crypto_data = data(sym)
    print(sym)
    fig = go.Figure(
        data = [
            go.Candlestick(
                x = crypto_data.index,
                open = crypto_data.Open,
                high = crypto_data.High,
                low = crypto_data.Low,
                close = crypto_data.Close
            ),
            go.Scatter(
                x = crypto_data.index, 
                y = crypto_data.Close.rolling(window=20).mean(),
                mode = 'lines', 
                name = '20SMA',
                line = {'color': '#ff006a'}
            ),
            go.Scatter(
                x = crypto_data.index, 
                y = crypto_data.Close.rolling(window=50).mean(),
                mode = 'lines', 
                name = '50SMA',
                line = {'color': '#1900ff'}
            )
        ]
    )
    fig.update_layout(
        title = f'The Candlestick graph for {sym}',
        xaxis_title = 'Date',
        yaxis_title = f'Price {sym}',
        xaxis_rangeslider_visible = False
    )
    fig.update_yaxes(tickprefix='$')
    # img=fig.to_image(format="png")
    # fig.write_image("images/fig1.png",format='png',engine='kaleido')
    # fig.write_image('images/fig1.png')

    fig.write_image("images/fig1.png",format='png',engine='kaleido')
    # fig.show()
    # fig.write_image("images/fig1.png",format='png',engine='kaleido')
    # return fig.to_image(format='png')
    # print(img)
    
    # return 
# Plot('BTC')

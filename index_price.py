import matplotlib.pyplot as plt
import matplotlib as mpl
import requests
import pandas as pd
import matplotlib.dates as mdates

API = '80d3b838cc53c0e158b45c873bd5cfb0d742696e42daf9d81ce12e39ef241a9a'


def get_indices(API: str):
    url = f'https://min-api.cryptocompare.com/data/index/list?api_key={API}'
    data = requests.get(url).json()['Data']
    return list(data.keys())


def get_index_price(index: str, limit: int):
    url = (
        'https://min-api.cryptocompare.com/data/index/histo/day?' +
        f'indexName={index}&limit={limit}&api_key={API}'
    )
    price = pd.DataFrame(requests.get(url).json()['Data'])
    price['time'] = pd.to_datetime(price['time'], unit='s')
    price.set_index('time', inplace=True)
    return price


def get_index_price_chart(index: str, limit: int):
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[
        '#00D666', '#0A2019', '#FF0066', '#00B0F0'
    ])
    data = get_index_price(index, limit)
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.plot(data['close'], lw=2)
    ax.fill_between(data.index, data['close'], alpha=0.4)

    plt.title(
        f'{index} {limit}-Day Performance',
        fontsize=28,
        fontname='Calibri',
        color='black',
        pad=5
    )
    plt.grid(visible=True, color='#D4D4D4')
    plt.xticks(weight='light', fontsize=24, fontname='Calibri')
    plt.yticks(weight='light', fontsize=20, fontname='Calibri')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.savefig(fr'resources\{index}_price.jpg')
    return


def get_performance_metrics(price: pd.DataFrame) -> pd.DataFrame:
    data = 
    return


if __name__ == '__main__':
    # indices = get_indices(API=API)
    get_index_price_chart(index='MVDA', limit=180)
    get_performanace

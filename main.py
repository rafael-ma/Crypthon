from binance.client import Client
import requests

# Chaves API
client = Client('wJTDbTGvtgepRORjxv1kmcvIKRPH81t9p0jbcZPp3u2hHgDTYEg27R2410huyRQy', 'lLWxz7OeS0a5jMUPCQL8cxqkaG5tSdKyj6QNqSQMGVECNzwZKOYbqCrWwloG9o7d')

coins = ['ETH', 'ADA', 'BNB', 'BTC', 'AVAX', 'LINK', 'SOL','BRL ']

# for coin in coins:
#     balance = client.get_asset_balance(asset=coin)
#     # print(f'Moeda: {balance['asset']} Quantidade:{balance['free']} Staked:{balance['locked']}')
#     print(balance)

# earnProducts = client.get_simple_earn_flexible_product_position()['rows']
# resultado = [item for item in earnProducts if item['asset'] == 'BNB']

for coin in coins:
    balance = client.get_asset_balance(asset=coin)
    if float(balance['free']) == 0 :
        earnProducts = client.get_simple_earn_flexible_product_position()['rows']
        balance = [item for item in earnProducts if item['asset'] == coin]

    print(balance)

from binance.client import Client
import requests

# Chaves API
client = Client('wJTDbTGvtgepRORjxv1kmcvIKRPH81t9p0jbcZPp3u2hHgDTYEg27R2410huyRQy', 'lLWxz7OeS0a5jMUPCQL8cxqkaG5tSdKyj6QNqSQMGVECNzwZKOYbqCrWwloG9o7d')

coins = ['ETH', 'ADA', 'BNB', 'BTC', 'AVAX', 'LINK', 'SOL']

# for coin in coins:
#     balance = client.get_asset_balance(asset=coin)
#     print(f'Moeda: {balance['asset']} Quantidade:{balance['free']} Staked:{balance['locked']}')

# Consultar ativos no Flexible Savings (Earn)

earnProducts = client.get_simple_earn_flexible_product_position()['rows']
for product in earnProducts:
    print(f'Moeda: {product['asset']} Quantidade: {product['totalAmount'].replace('.', ',')} Ganho Anual: {product['latestAnnualPercentageRate'].replace('.', ',')}%')
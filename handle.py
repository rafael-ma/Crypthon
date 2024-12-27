import requests

# URL do endpoint de informações da exchange
url = "https://api.binance.com/api/v3/exchangeInfo"

# Fazendo a requisição
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    symbols = data.get("symbols", [])
    print(symbols[0])
    
    # Procura o par desejado (exemplo: BTCUSDT)
    for symbol in symbols:
        if symbol["symbol"] == "BTCUSDT":
            print(f"Par de negociação: {symbol['symbol']}")
            for filter in symbol["filters"]:
                if filter["filterType"] == "LOT_SIZE":
                    print(f"Tamanho mínimo de ordem: {filter['minQty']}")
                if filter["filterType"] == "MIN_NOTIONAL":
                    print(f"Valor mínimo notional: {filter['minNotional']}")
            break
else:
    print(f"Erro na requisição. Código: {response.status_code}")
    print("Mensagem:", response.text)

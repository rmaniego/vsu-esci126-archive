"""
Python Dictionaries
 - A data structure, or a method to store data in RAM.
 - A structured data is faster versus unorganized data.
 - The data supplied in
 - Contains key-value pairs.
"""

cryptocurrencies = {
    "0x": "ZRX",
    "1inch": "1inch",
    "aave": "Aave",
    "ada": "Cardano",
    "algo": "Algorand",
    "ampl": "Ampleforth",
    "ankr": "Ankr",
    "atom": "Cosmos",
    "bal": "Balancer",
    "band": "Band Protocol",
    "bch": "Bitcoin Cash",
    "bnt": "Bancor Network Token",
    "btc": "Bitcoin",
    "comp": "Compound",
    "crv": "Curve DAO Token",
    "cvc": "Civic",
    "dai": "DAI",
    "dash": "Dash",
    "dnt": "district0x",
    "enj": "Enjin Coin",
    "eos": "EOS",
    "etc": "Ethereum Classic",
    "eth": "Ethereum",
    "forth": "Ampleforth Governance Token",
    "grt": "The Graph",
    "knc": "Kyber Network",
    "link": "Chainlink",
    "lrc": "Loopring",
    "ltc": "Litecoin",
    "mana": "Decentraland",
    "matic": "Polygon",
    "mkr": "Maker",
    "nkn": "NKN",
    "nmr": "Numeraire",
    "nu": "NuCypher",
    "ogn": "Origin Protocol",
    "omg": "OMG Network",
    "oxt": "Orchid Protocol",
    "ren": "REN",
    "rep": "Augur",
    "skl": "SKALE",
    "snx": "Synthetix Network Token",
    "storj": "Storj",
    "sushi": "Sushi",
    "uma": "UMA",
    "uni": "UniSwap",
    "wbtc": "Wrapped Bitcoin",
    "xlm": "Stellar Lumens",
    "xrp": "XRP",
    "xtz": "Tezos",
    "yfi": "yearn.finance",
    "zec": "Zcash"
}

print("\nSupported Tokens:")

# Looping over a dictionary
# for key, value in variable.items():
for key, coin in cryptocurrencies.items():
    print(f" * {coin} ({key})")
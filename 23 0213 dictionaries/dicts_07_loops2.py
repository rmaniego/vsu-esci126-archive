"""
Python Dictionaries
 - A data structure, or a method to store data in RAM.
 - A structured data is faster versus unorganized data.
 - The data supplied in
 - Contains key-value pairs.
"""

cryptocurrencies = {
    "0x": {
        "id": "0x",
        "name": "ZRX",
    },
    "1inch": {
        "id": "1inch",
        "name": "1inch",
    },
    "aave": {
        "id": "aave",
        "name": "Aave",
    },
    "ada": {
        "id": "cardano",
        "name": "Cardano",
    },
    "algo": {
        "id": "algorand",
        "name": "Algorand",
    },
    "ampl": {
        "id": "ampleforth",
        "name": "Ampleforth",
    },
    "ankr": {
        "id": "ankr",
        "name": "Ankr",
    },
    "atom": {
        "id": "cosmos",
        "name": "Cosmos",
    },
    "bal": {
        "id": "balancer",
        "name": "Balancer",
    },
    "band": {
        "id": "band-protocol",
        "name": "Band Protocol",
    },
    "bch": {
        "id": "bitcoin-cash",
        "name": "Bitcoin Cash",
    },
    "bnt": {
        "id": "bancor",
        "name": "Bancor Network Token",
    },
    "btc": {
        "id": "bitcoin",
        "name": "Bitcoin",
    },
    "comp": {
        "id": "compound-governance-token",
        "name": "Compound",
    },
    "crv": {
        "id": "curve-dao-token",
        "name": "Curve DAO Token",
    },
    "cvc": {
        "id": "civic",
        "name": "Civic",
    },
    "dai": {
        "id": "dai",
        "name": "DAI",
    },
    "dash": {
        "id": "dash",
        "name": "Dash",
    },
    "dnt": {
        "id": "district0x",
        "name": "district0x",
    },
    "enj": {
        "id": "enjincoin",
        "name": "Enjin Coin",
    },
    "eos": {
        "id": "eos",
        "name": "EOS",
    },
    "etc": {
        "id": "ethereum-classic",
        "name": "Ethereum Classic",
    },
    "eth": {
        "id": "ethereum",
        "name": "Ethereum",
    },
    "forth": {
        "id": "ampleforth-governance-token",
        "name": "Ampleforth Governance Token",
    },
    "grt": {
        "id": "the-graph",
        "name": "The Graph",
    },
    "knc": {
        "id": "kyber-network",
        "name": "Kyber Network",
    },
    "link": {
        "id": "chainlink",
        "name": "Chainlink",
    },
    "lrc": {
        "id": "loopring",
        "name": "Loopring",
    },
    "ltc": {
        "id": "litecoin",
        "name": "Litecoin",
    },
    "mana": {
        "id": "decentraland",
        "name": "Decentraland",
    },
    "matic": {
        "id": "matic-network",
        "name": "Polygon",
    },
    "mkr": {
        "id": "maker",
        "name": "Maker",
    },
    "nkn": {
        "id": "nkn",
        "name": "NKN",
    },
    "nmr": {
        "id": "numeraire",
        "name": "Numeraire",
    },
    "nu": {
        "id": "nucypher",
        "name": "NuCypher",
    },
    "ogn": {
        "id": "origin-protocol",
        "name": "Origin Protocol",
    },
    "omg": {
        "id": "omisego",
        "name": "OMG Network",
    },
    "oxt": {
        "id": "orchid-protocol",
        "name": "Orchid Protocol",
    },
    "ren": {
        "id": "republic-protocol",
        "name": "REN",
    },
    "rep": {
        "id": "augur",
        "name": "Augur",
    },
    "skl": {
        "id": "skale",
        "name": "SKALE",
    },
    "snx": {
        "id": "havven",
        "name": "Synthetix Network Token",
    },
    "storj": {
        "id": "storj",
        "name": "Storj",
    },
    "sushi": {
        "id": "sushi",
        "name": "Sushi",
    },
    "uma": {
        "id": "uma",
        "name": "UMA",
    },
    "uni": {
        "id": "uniswap",
        "name": "UniSwap",
    },
    "wbtc": {
        "id": "wrapped-bitcoin",
        "name": "Wrapped Bitcoin",
    },
    "xlm": {
        "id": "stellar",
        "name": "Stellar Lumens",
    },
    "xrp": {
        "id": "ripple",
        "name": "XRP",
    },
    "xtz": {
        "id": "tezos",
        "name": "Tezos",
    },
    "yfi": {
        "id": "yearn-finance",
        "name": "yearn.finance",
    },
    "zec": {
        "id": "zcash",
        "name": "Zcash",
    }
}

print("Token IDs:")

# Parse the value 
for key, coin in cryptocurrencies.items():
    
    coin_id = coin["id"]
    coin_name = coin["name"]
    
    print(f" * {coin_name} ({key}): {coin_id}")
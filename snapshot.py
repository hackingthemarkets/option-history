import config, requests, pprint, sqlite3
from datetime import datetime

connection = sqlite3.connect('option_history.db')
cursor = connection.cursor()

try:
    cursor.execute("""
        CREATE TABLE option_history (
            timestamp text,
            underlying text,
            symbol text,
            description text,
            strike real,
            bid real,
            ask real
        )
    """)
except:
    pass


response = requests.get(config.OPTION_CHAIN_URL,
    params={'symbol': 'AAPL', 'expiration': '2020-07-10'},
    headers=config.HEADERS
)

json_response = response.json()
options = json_response['options']['option']

current_timestamp = datetime.now().replace(second=0, microsecond=0).isoformat()

for option in options:
    data = (current_timestamp, option['underlying'], option['symbol'], option['description'], option['strike'], option['bid'], option['ask'])

    print(",".join(map(str, data)))

    cursor.execute("""
        INSERT INTO option_history (
            timestamp, underlying, symbol, description, strike, bid, ask
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)

connection.commit()
connection.close()
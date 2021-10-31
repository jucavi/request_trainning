import requests
import json

BASE_URL = 'https://ftx.com/api/'

fnames = ['markets', 'futures', 'nft/nfts']

for name in fnames:
    url = f'{BASE_URL}{name}'
    
    try:
        data = requests.get(url).json()
    except Exception as e:
        print(f'Error getting {url}: {e}')
    else:
        if data['success']:
            if name.startswith('nft'):
                name = name.replace('nft/', '')
                
            file_name = f'{name}.json'
            with open(file_name, 'w') as file:
                print(f'Writing {file.name}')
                file.write(json.dumps(data['result'], indent=2))
        else:
            print(data['error'])
import requests
from bs4 import BeautifulSoup
import json

def cleanpercent(value):
    value = value.replace('%', '').strip()
    if value.startswith('<'):
        return 0.01
    try:
        return float(value)
    except ValueError:
        return None

def GetCryptoDetails():
    soup = None
    data = {}
    deviation = 0.1  # Deviation threshold in percent

    res = requests.get("https://coinmarketcap.com/all/views/all/")
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html5lib')
        tablerows = soup.find_all('tr', class_='cmc-table-row')

        try:
            i = 0
            for tablerow in tablerows:
                try:
                    coinname_elem = tablerow.find('td', class_=lambda x: x and 'name' in x)
                    if not coinname_elem:
                        continue
                    
                    coinname = coinname_elem.text.strip().split(" ")
                    coinname = coinname[0] + coinname[-1].replace("\n", '')

                    weekchange_elem = tablerow.find('td', class_=lambda x: x and 'change-24-h' in x)
                    if not weekchange_elem:
                        continue
                    
                    weekchange = cleanpercent(weekchange_elem.text.strip().split(" ")[0].replace("\n", ''))
                    if weekchange is None:
                        continue

                    detail = {
                        'coinname': coinname[:(len(coinname)//2)],
                        'weekchange': weekchange,
                        'status': 'postitive' if weekchange > 0 else 'negative'
                    }
                    if abs(weekchange) >= deviation:
                        i += 1
                        data[str(i)] = detail

                except Exception as e:
                    print(f'Error parsing row: {e}')
                    return 'fail'
            
            print('Operation Done')

        except Exception as e:
            print(f'Error in outer loop: {e}')
            return 'fail'

    else:
        print(f"Request failed with status: {res.status_code}")
        return 'fail'

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Saved data successfully")
    return 'success'


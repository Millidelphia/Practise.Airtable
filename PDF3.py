import requests
import os
import shutil

base_id = 'appx3BTpqW1UAIzDz'
table_id = 'tblC186rO1LJqs6gf'
personal_access_token = 'patEPV6wnalYglZx0.b49e81cb57ad7117480f72fe5de815e2ec5814895f38ec5a428a7fa2a937edff'

url = f'https://api.airtable.com/v0/appx3BTpqW1UAIzDz/tblC186rO1LJqs6gf'
headers = {
    'Authorization': f'Bearer patEPV6wnalYglZx0.b49e81cb57ad7117480f72fe5de815e2ec5814895f38ec5a428a7fa2a937edff'
}

response = requests.get(url, headers=headers)
records = response.json()['records']

for record in records:
    file_name = record['fields']['Скан ВКР'][0]['filename']
    file_url = record['fields']['Скан ВКР'][0]['url']
    response = requests.get(file_url)
    file_dir = os.path.join('C:', 'Практика', 'ПДФ 3 Часть') 
    os.makedirs(file_dir, exist_ok=True)  
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)
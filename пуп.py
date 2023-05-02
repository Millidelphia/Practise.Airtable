import os
import pandas as pd
import requests
import json
import re


df = pd.read_excel('Все1.xlsx')


for index, row in df.iterrows():
    
    file_info = json.loads(row['Скан ВКР'].replace('\\', '\\\\').replace("'", "\""))
    
    if file_info:
        
        file_url = file_info[0]['url']
        
        file_name = file_info[0]['filename']
        
        file_name = re.sub(r'[^\w\s\.\(\)-]', '', file_name)
        
        response = requests.get(file_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        file_dir = os.path.join('S:', 'Практика', 'pdf файлы')
        os.makedirs(file_dir, exist_ok=True)
        
        file_path = os.path.join(file_dir, file_name)
        
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Файл {file_name} загружен')
    else:
        print(f'Для строки {index} ссылка на файл отсутствует')





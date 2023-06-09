import os
import pandas as pd
import requests
import json


df = pd.read_excel('Все2.xlsx')


for index, row in df.iterrows():
    
    file_info = row['Скан ВКР']
    
    if isinstance(file_info, str):
        file_info = json.loads(file_info.replace('\\', '\\\\').replace("'", "\""))
        
        file_url = file_info[0]['url']
        
        file_name = str(file_info[0]['filename'])
        
        file_name = file_name.translate(str.maketrans('\\/:*?"<>|', '_________'))
        
        file_name = os.path.normpath(file_name)
        
        try:
            response = requests.get(file_url, headers={'User-Agent': 'Mozilla/5.0'})
        except requests.exceptions.ConnectionError as e:
            print(f'Ошибка загрузки файла: {e}')
            continue
        
        file_dir = os.path.join('S:', 'Практика', 'pdf файлы')
        os.makedirs(file_dir, exist_ok=True)
        
        file_path = os.path.join(file_dir, file_name)
        
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Файл {file_name} загружен')
    else:
        print(f'Для строки {index} ссылка на файл отсутствует')


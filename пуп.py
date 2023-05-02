import os
import pandas as pd
import requests
import json

# загружаем таблицу excel
df = pd.read_excel('Все1.xlsx')

# проходим по строкам таблицы
for index, row in df.iterrows():
    # получаем информацию о файле из столбца 'Скан ВКР'
    file_info = json.loads(row['Скан ВКР'].replace('\\', '\\\\').replace("'", "\""))
    # проверяем, есть ли ссылки на файлы в ячейке
    if file_info:
        # получаем url файла из первого словаря в списке
        file_url = file_info[0]['url']
        # получаем имя файла из первого словаря в списке
        file_name = file_info[0]['filename']
        # загружаем файл
        response = requests.get(file_url, headers={'User-Agent': 'Mozilla/5.0'})
        # создаем папку, если ее нет
        file_dir = os.path.join('S:', 'Практика', 'pdf файлы2')
        os.makedirs(file_dir, exist_ok=True)
        # создаем полный путь к файлу
        file_path = os.path.join(file_dir, file_name)
        # сохраняем файл на диск
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Файл {file_name} загружен')
    else:
        print(f'Для строки {index} ссылка на файл отсутствует')






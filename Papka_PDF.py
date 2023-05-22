import os
import fitz  
from collections import Counter
import shutil
import re

pdf_folder = 'S:\\practika\\Практика\\pdf файлы'
output_folder = 'S:\\practika\\Papka\\pdf_rasp1'

# Преобр имени str в папку
def sanitize_folder_name(folder_name):
    sanitized_name = re.sub(r'[\\/:*?"<>|]', '_', folder_name)
    
    sanitized_name = sanitized_name.replace('-', '')
    sanitized_name = sanitized_name.replace('–', '')
    sanitized_name = sanitized_name.replace('«', '')
    sanitized_name = sanitized_name.replace('»', '')
    sanitized_name = sanitized_name.replace(' ', '')
    sanitized_name = sanitized_name.replace(',', '.')
    return sanitized_name


line_counter = Counter()


for file_name in os.listdir(pdf_folder):
    if file_name.endswith('.pdf'):
        #open
        pdf_path = os.path.join(pdf_folder, file_name)
        pdf_file = fitz.open(pdf_path)

        
        first_page = pdf_file[0]
        text = first_page.get_text()

        #fraza
        search_text = 'Вид выпускной квалификационной работы:'
        start_index = text.find(search_text)
        if start_index != -1:
            
            next_line_start = text.find('\n', start_index) + 1
            next_line_end = text.find('\n', next_line_start)
            
            
            next_line_start = text.find('\n', next_line_end) + 1
            next_line_end = text.find('\n', next_line_start)

            
            next_line = text[next_line_start:next_line_end].strip()
            
            
            line_counter[next_line] += 1
            
            
            sanitized_folder_name = sanitize_folder_name(next_line)
            
            
            output_path = os.path.join(output_folder, sanitized_folder_name)
            if not os.path.exists(output_path):
                os.makedirs(output_path) 
            
            new_file_path = os.path.join(output_path, file_name)
            shutil.copy(pdf_path, new_file_path)

        pdf_file.close()



print("Подсчет и распределение:")
for line, count in line_counter.items(): 
    print(f"Строка: {line}, Количество: {count}")


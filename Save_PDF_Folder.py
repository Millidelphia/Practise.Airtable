import os
import fitz
from collections import Counter
import shutil
import re

pdf_folder = 'S:\\practika\\Papka\\pdf файлы'
output_folder = 'S:\\practika\\Papka\\pdf_rasp1'

# Преобразование имени str в имя папки
def sanitize_folder_name(folder_name):
    sanitized_name = re.sub(r'[\\/:*?"<>|]', '_', folder_name)
    sanitized_name = sanitized_name.replace('-', '')
    sanitized_name = sanitized_name.replace('–', '')
    sanitized_name = sanitized_name.replace('«', '')
    sanitized_name = sanitized_name.replace('»', '')
    sanitized_name = sanitized_name.replace(',', '.')

    # Добавляем точки между каждыми двумя цифрами
    sanitized_name = re.sub(r'(\d{2})', r'\1.', sanitized_name)
    return sanitized_name


line_counter = Counter()
files_not_in_folders = []

for file_name in os.listdir(pdf_folder):
    if file_name.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, file_name)
        pdf_file = fitz.open(pdf_path)

        first_page = pdf_file[0]
        text = first_page.get_text()

        search_text = 'Вид выпускной квалификационной работы:'
        start_index = text.find(search_text)
        if start_index != -1:
            next_line_start = text.find('\n', start_index) + 1
            next_line_end = text.find('\n', next_line_start)

            next_line_start = text.find('\n', next_line_end) + 1
            next_line_end = text.find('\n', next_line_start)

            current_line = text[next_line_start:next_line_end].strip()

            if not any(char.isdigit() for char in current_line):
                next_line_start = text.find('\n', next_line_end) + 1
                next_line_end = text.find('\n', next_line_start)

                next_line = text[next_line_start:next_line_end].strip()

                if any(char.isdigit() for char in next_line):
                    current_line = next_line

            # Проверяем, содержит ли строка цифры
            if any(char.isdigit() for char in current_line):
                # Получаем только текст после фразы 'Вид выпускной квалификационной работы:'
                next_line = re.sub(r'\D', '', current_line)

                line_counter[next_line] += 1

                sanitized_folder_name = sanitize_folder_name(next_line)
                output_path = os.path.join(output_folder, sanitized_folder_name)

                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                new_file_path = os.path.join(output_path, file_name)
                shutil.copy(pdf_path, new_file_path)
            else:
                files_not_in_folders.append(file_name)

        pdf_file.close()

print("Подсчет и распределение:")
for line, count in line_counter.items():
    print(f"Строка: {line}, Количество: {count}")

print("Количество файлов, не входящих в папки:", len(files_not_in_folders))


















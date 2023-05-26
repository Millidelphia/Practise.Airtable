import os
import fitz  # PyMuPDF
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt


stop_words = set(stopwords.words('russian'))


all_word_counts = {}

# Проходим по каждому PDF-файлу
pdf_folder = 'S:\practika\Практика\pdf файлы'
for file_name in os.listdir(pdf_folder):
    if file_name.endswith('.pdf'):
        # Открываем PDF-файл
        pdf_path = os.path.join(pdf_folder, file_name)
        pdf_file = fitz.open(pdf_path)

        
        for page in pdf_file:
            text = page.get_text()

            
            words = word_tokenize(text, language='russian')

            # Удаляем стоп-слова и пунктуацию
            filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

            # Считаем количество каждого слова и добавляем его в словарь all_word_counts
            for word in filtered_words:
                all_word_counts[word] = all_word_counts.get(word, 0) + 1

        pdf_file.close()

# Выводим список наиболее употребляемых слов и их количество во всех файлах
print("Words in all files:")
for word, count in Counter(all_word_counts).most_common(30):
    print(f"{word}: {count}")

# Получаем список слов и количество упоминаний для наиболее употребляемых слов
words = [word for word, count in Counter(all_word_counts).most_common(30)]
word_counts = [count for word, count in Counter(all_word_counts).most_common(30)]

# Создаем график
plt.figure(figsize=(10, 6))
plt.bar(words, word_counts)
plt.xlabel('Words')
plt.ylabel('Count')
plt.title('Top 30 Most Common Words')
plt.xticks(rotation=60)

# Отображаем график
plt.show()


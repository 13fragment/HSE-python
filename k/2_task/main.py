import os
import glob
from collections import Counter

directory = "/home/max/PycharmProjects/HSE-python/k/2_task"

files_list = glob.glob(os.path.join(directory, '*.txt'))

if len(files_list) < 3:
    print('В заданном каталоге недостаточно файлов')
    exit()

all_words = []

for file in files_list:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip().split()
            all_words.extend(words)

word_counts = Counter(all_words)
most_common_word = word_counts.most_common(1)[0][0]

print('Наиболее часто встречающееся слово во всех файлах:', most_common_word)
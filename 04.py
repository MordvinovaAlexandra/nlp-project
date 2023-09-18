'''дан текстовый файл, надо создать новый, в который 
надо перезаписать из исходного все слова, в которых не менее 7 букв'''

import re

with open('./TEXT/01.txt',encoding = 'utf-8') as f:
    text = f.read()
# words = re.split(r'\W+', text)
words = re.findall(r'\w{7,}', text)
# long_words = []
# for word in words:
#     if len(word)>=7:
#         long_words.append(word)
# print(long_words)
# print(words)
with open('./TEXT/04.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(word + '\n' for word in words)
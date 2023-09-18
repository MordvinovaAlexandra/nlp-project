# with open('./TEXT/01.txt',encoding = 'utf-8') as f:
#     print(f.read(10))
#     f.seek(8)
#     print(f.read(10))

# print(f.read()) #выдаст ошибку, т.к. файл уже закрыт

try:
    with open('./TEXT/02.txt',encoding = 'utf-8') as f:
        print(f.read(10))
        f.seek(8)
        print(f.read(10))
except FileNotFoundError:
    print('File not found')

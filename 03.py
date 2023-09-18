with open('./TEXT/02.txt', 'w') as f:
    f.write('test')
    f.write('\nmeow')
    f.seek(0)
    f.write('2')
with open('./TEXT/02.txt', 'a') as f:
    f.write('\nappend')
# with open('./TEXT/02.txt', 'x') as f:
#     f.write('\nx')

#первый способ добавления переноса строки:
# with open('./TEXT/03.txt', 'w') as f:
#     lines = ('line1\n', 'line2\n', 'line3')
#     f.writelines(lines)
#2 способ переноса строки:
with open('./TEXT/03.txt', 'w') as f:
    lines = ('line1', 'line2', 'line3')
    f.writelines([line + '\n' for line in lines])
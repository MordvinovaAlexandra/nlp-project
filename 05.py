'''дан текст, необходимо переписать его в другой:
1) порядок строк должен совпадать с порядком строк
2) порядок строк должен быть реверсивным'''

#1 вариант, простой:

# with open('./TEXT/05.txt',encoding = 'utf-8') as f:
#     lines = f.readlines()

# with open('./TEXT/05_out.txt', 'w', encoding = 'utf-8') as f:
#     f.writelines(lines)

#2 вариант - обработка построчно:

# with open('./TEXT/05.txt',encoding = 'utf-8') as f_in:
#     with open('./TEXT/05_out.txt', 'w', encoding = 'utf-8') as f_out:
#         for line in f_in:
#             f_out.write(line)

# обратный порядок:
def write_line(f_in, f_out):
    for line in f_in:
        write_line(f_in, f_out)
        f_out.write(line)


with open('./TEXT/05.txt',encoding = 'utf-8') as f_in:
    with open('./TEXT/05_out.txt', 'w', encoding = 'utf-8') as f_out:
        write_line(f_in, f_out)
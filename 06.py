'''Дан текст, добавить в него строку из 12 звездочек, 
поместив ее после последней из строк, в которых нет запятой, если таких строк нет, 
то новая строка должна быть добавлена после всех строк файла. Результат записать в другой файл'''

with open('./TEXT/05.txt',encoding = 'utf-8') as f_in:
    with open('./TEXT/06_out.txt', 'w', encoding = 'utf-8') as f_out:
        last_row = -1
        for row_ix, line in enumerate(f_in):
            if ',' not in line:
                last_row = row_ix

        if last_row ==-1:
            f_in.seek(0)
            f_out.write(f_in.read())
            f_out.write('\n************')
        else:
            f_in.seek(0)
            for row_ix, line in enumerate(f_in):
                f_out.write(line)
                if row_ix == last_row:
                    f_out.write('************\n')


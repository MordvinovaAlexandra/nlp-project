'''Дан текстовый файл, в нем надо заменить все * на &'''
with open('./TEXT/07.txt',encoding = 'utf-8') as f_in:
    with open('./TEXT/07_out.txt', 'w', encoding = 'utf-8') as f_out:
        while ch:= f_in.read(1):
            if ch == '&':
                f_out.write('*')
            elif ch == '*':
                f_out.write('&')
            else:
                f_out.write(ch)
            


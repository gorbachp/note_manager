#Вводные данные пользователя
username = input('Введите ваше имя: ')
title1 = input('Введите заголовок 1-ой заметки: ')
title2 = input('Введите заголовок 2-ой заметки: ')
title3 = input('Введите заголовок 3-ей заметки: ')
title_list = [title1, title2, title3]
content = input('Опишите заметку: ')
status = input('Введите статус заметки: ')
created_date = input('Напишите дату создания заметки (в формате дд-мм-гггг): ')
issue_date = input('Напишите дату окончания заметки (в формате дд-мм-гггг): ')

#Список введенных данных от пользователя
note = [
    username,
    title_list,  # список для заголовков
    content,
    status,
    created_date,
    issue_date
]

#Вывод вводных данных пользователя
print('Ваше имя:', username)
print('Заголовки заметки:', title_list)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания:', created_date[0:5])
print('Дата окончания:', issue_date[0:5])

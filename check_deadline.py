from datetime import datetime

# Основной код программы
while True:
    try:
        # Запрашиваем текущую дату
        current_date = datetime.now()
        # Запрашиваем у пользователя дату дедлайна
        deadline_input = input('Напишите дату создания заметки (в формате дд-мм-гггг, например 27-11-2024):')
        # Преобразуем строку input в datetime
        deadline_date = datetime.strptime(deadline_input, format('%d-%m-%Y'))
        # Вычисляем разницу между текущей датой и дедлайном в днях
        time_difference = (deadline_date - current_date)
        days_difference = time_difference.days

        # Выводим информацию о дедлайне и сроке окончания
        if days_difference < 0:
            print(f'ВНИМАНИЕ! Дедлайн истек {abs(days_difference)} дня(ей) назад!')
        elif days_difference == 0:
            print('Дедлайн сегодня!')
        else:
            print(f'Дедлайн через {days_difference} дня(ей)!')

        break  # Выход из цикла при корректной работе

    # Выводим ошибку при некорректном вводе даты
    except ValueError:
        print('Ошибка! Неверный формат даты. Напишите дату в формате дд-мм-гггг.')
        print('Пример: 27-11-2024')

    # Выводим ошибку при других обстоятельствах
    except Exception as error:
        print(f'Произошла непредвиденная ошибка: {error}')
        print('Попробуйте снова.')



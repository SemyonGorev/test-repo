def month_to_season(month):

    if 2 < month and month < 6:

        print('Весна')

    elif 5 < month and month < 9:

        print('Лето')

    elif 8 < month and month < 12:

        print('Осень')

    elif month == 12 or month < 3 and month > 0:

        print('Зима')

    else:

        print('Некорректный номер месяца')

month_to_season(1)
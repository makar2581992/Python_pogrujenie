# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

check1 = 4
check2 = 100
check3 = 400
grig_year = 1582
result = ''
year = int(input('Введите год: '))
if year < grig_year:
    result = 'Введена некорректная дата'
elif year % check1:
    result = 'Год обычный'
elif not year % check2:
    if not year % check3:
        result = 'Високосный'
    else:
        result = 'Обычный'
else:
    result = 'Високосный'
print(result)
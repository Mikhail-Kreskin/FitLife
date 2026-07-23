# Проект FitLife - MVP версия 1.1

WATER_PER_KG = 30
ML_IN_L = 1000

while True:
    user_name = input('Введите Ваше имя: ').strip()
    if user_name == '':
        print('Пожалуйста, введите Ваше имя')
    else:
        user_name = user_name
        break


while True:
    try:
        user_age = int(input('Введите Ваш возраст: '))
        break
    except (ValueError, NameError):
        print('Введите Ваш возраст используя цифры')


while True:
    try:
        user_weight = float(input('Введите Ваш вес(кг), используя точку: '))
        if user_weight == 0:
            print('Вес не может быть равен 0')
        else:
            user_weight = user_weight
            break
    except (ValueError, NameError):
        print('Введите Ваш вес используя цифры с точкой')

while True:
    try:
        user_height = float(input('Введите Ваш рост(м), используя точку: '))
        if user_height == 0:
            print('Рост не может быть равен 0')
        else:
            user_height = user_height
            break
    except (ValueError, NameError):
        print('Введите рост используя цифры с точкой')


# Расчёт индекса массы тела
bmi = round((user_weight / user_height ** 2), 1)

# Расчет воды в мл
water_ml = user_weight * WATER_PER_KG

# Расчет воды в л
water_l = round((water_ml / ML_IN_L), 1)

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела(ИМТ): {bmi}')
print('Что показывает Ваш ИМТ:')

if bmi <= 16.0:
    print('У вас выраженный дефицит массы тела')

elif 16.1 <= bmi <= 18.5:
    print('У вас недостаточная масса тела')

elif 18.6 <= bmi <= 24.9:
    print('У вас нормальная масса тела')

elif 25.0 <= bmi <= 29.9:
    print('У вас избыточная масса тела')

elif 30.0 <= bmi <= 34.9:
    print('У вас ожирение 1 степени')

elif 35.0 <= bmi <= 39.9:
    print('У вас ожирение 2 степени')

else:
    print('У вас ожирение 3 степени')

print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')

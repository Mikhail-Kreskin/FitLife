# Проект FitLife - MVP версия 1.0

user_name = input('Введите Ваше имя: ').capitalize()
user_age = int(input('Введите Ваш возраст: '))

try:
    user_weight = float(input('Введите Ваш вес(кг), используя точку: '))
    user_height = float(input('Введите Ваш рост(м), используя точку: '))

except ValueError:
    print('Введите Ваш вес и рост используя цифры с ' \
    'точкой в качестве разделителя\nВес и рост не могут быть равны 0')


WATER_PER_KG = 30
ML_IN_L = 1000

#Расчёт индекса массы тела
bmi = round((user_weight / user_height ** 2), 1)

#Расчет воды в мл
water_ml = user_weight * WATER_PER_KG

#Расчет воды в л
water_l = round((water_ml / ML_IN_L), 1)

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print(f'Расчет окончен. Будьте здоровы!')
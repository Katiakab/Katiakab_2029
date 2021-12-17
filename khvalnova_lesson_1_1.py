duration = int(input('Введите время в секундах: '))
min = int(duration / 60)
hour = int(duration / 3600)
day = int(duration / 86400)
print(duration, 'секунд')
print(min, 'минут', duration % 60, 'секунд.')
print(hour, 'часов', min % 60, 'минут', duration % 60, 'секунд.')
print(day, 'дней', hour % 24, 'часов', min % 60, 'минут', duration % 60, 'секунд.')

# с использованием if-elif-else
duration = int(input('Введите время в секундах'))
sec_in_min = 60
sec_in_hour = sec_in_min * 60   # 3600
sec_in_day = sec_in_hour * 24   #86400
min = int(duration/sec_in_min)
hour = int(duration/sec_in_hour)
day = int(duration/sec_in_day)

if duration < sec_in_min:
    print(duration, 'сек.')
elif duration < sec_in_hour:
    print(min, 'мин.', duration % 60, 'сек.')
elif duration < sec_in_day:
    print(hour, 'час.', min % 60, 'мин.', duration % 60, 'сек.')
else:
    print(day, 'дн.', hour % 24, 'час.', min % 60, 'мин.', duration % 60, 'сек.')
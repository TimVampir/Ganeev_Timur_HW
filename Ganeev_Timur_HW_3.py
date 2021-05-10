percent = int(input('Введите количество процентов от 1 до 20: '))
if percent in range(5, 21):
    print(percent, 'процентов')
elif percent in range(2, 5):
    print(percent, 'процента')
else:
    print(percent, 'процент')
'''
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''
num = int(input("Введите число: "))
word = ''
digit = num % 10.

if digit in [0, 5, 6, 7, 8, 9]:
    word = 'процентов'
elif digit == 1:
    word = 'процент'
elif digit in [2, 3, 4]:
    if num < 20 and num > 10:
        word = 'процентов'
    else:
        word = 'процента'

print('{0} {1}'.format(num, word))
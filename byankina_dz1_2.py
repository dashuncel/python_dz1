'''
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
'''

my_list = []
i = 1
summa = 0

while i < 1000:
    if i % 2 != 0:
        my_list.append(i ** 3)
    i += 1

for dec in my_list:
    tmp_sum = 0
    while dec > 0:
        digit = dec % 10
        tmp_sum += digit
        dec = dec // 10
    if tmp_sum % 7 == 0:
        summa += tmp_sum

print(summa)
'''
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
сделать оптимизацию кода по памяти, по скорости.
'''

src = [200, 201, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 77, 12, 13, 11, 18]

result = [num for key, num in enumerate(src) if (key > 0 and src[key-1] < num)]
print(result)


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
print('Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону')
print('т.е. не меньше заданного минимума и не больше заданного максимума')
print('Массив: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]')
Num_min=int(input('Введите минимальное значение: '))
Num_max=int(input('Введите максимальное значение: '))
array=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
arraysorted=[]
arrayindex=[]

for i in range(len(array)):
    if array[i]>Num_min and array[i]<Num_max:
        arraysorted.append(array[i])
        arrayindex.append(i)
        

print('Индексы элементов не меньших ', Num_min, 'и не больших ', Num_max)
print(arrayindex)
print('Это элементы:')
print(arraysorted)


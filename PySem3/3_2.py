# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

N=int (input('Введите число N, которое задаст размер массива A[1..N]: '))
X=int (input('Введите число X, ближайшее к которому мы будем искать в массиве: '))
A=[]
j=1
flag=True

for i in range(N):
   A.append(random.randint(1,9))
  
print (A)

while flag:
    for i in range(N):
        if abs(X-A[i])==j:
            NearestNum=A[i]
            flag=False
    j+=1    

print ('элемент массива ',NearestNum)
print ('наиболее близок к числу ',X)

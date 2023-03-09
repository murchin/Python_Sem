# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def Degree_Num(A,B):
    Result=0
    if B==1:
        return A
    else:
        Result= A*Degree_Num(A,B-1)
        return Result


A=int(input('Введите число А: '))
B=int(input('Введите число В: '))

print(Degree_Num(A,B))
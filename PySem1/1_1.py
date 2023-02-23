# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number= input("Введите трехзначное положительное число:") 
if (number[0]=='-'):
    print('Вы пытаетесь ввести значение меньше 0. Так не пойдет. Мы сделаем его положительным.')
    number=number.replace('-','' )
    print('Вот так:', number)

if ('.' in number):
    print('Вы пытаетесь ввести дробь. Нас не проведешь!')
    number=number[:number.find('.')]
    print('Сделаем вот так:', number)
    

if (number.isdigit()):
    if (int (number) > 99) and (int (number) < 1000):
        SumOfElements = int (number[0]) + int(number[1]) + int(number[2])
        print("Сумма цифр числа", number,"равна", SumOfElements)
    else:
        print('Вы ввели не трехзначное число')
else: 
    print('Вы ввели не число')
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.
print('Загаданы 2 натуралных числа. Известна их сумма и произведение. Отгадаем эти числа')

flag = True

while flag:
    S=(input('Введите сумму чисел:'))
    P=(input('Введите произведение чисел:'))
    if S.isdigit()==True and P.isdigit()==True:
        if int(S)>0 and int(P)>0: 
            S= int(S)
            P= int(P)
            flag=False
        else:
            print ('Эти числа не подходят! Оба числа должны быть натуральными!')
    else:
        print('Эти числа не подходят. Оба числа должны быть целыми!')

d=S**2-4*P

if d<0:
    print('Таких натуральных чисел нет!')
elif d>0:
    x1=(S+(d**(0.5)))/2
    x2=(S-(d**(0.5)))/2
    if int(x1)==x1 and int(x2)==x2:
        y1=S-x1
        y2=S-x2
        print('Были загаданы числа:',x1,'  ',y1, ' или ', x2, '  ', y2)
    else:
        print ('Таких натуральных чисел нет')
elif d==0:
    x1=(S+(d**(0.5)))/2
    y1=S-x1
    print('Были загаданы числа:',x1,'  ',y1)
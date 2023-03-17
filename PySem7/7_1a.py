# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
aoe=['у','е','ы','а','о','э','я','и','ю']
text=((input('Введите кричалку: ')).lower()).split()
print(text)
counter=0
end=[]

for index, value in enumerate(text):
    for index1, value1 in enumerate(text[index]):
        if value1 in aoe:
            counter+=1
    end.append(counter)
    counter=0
    
for i in range(1,len(end)):
    if end[0]!=end[i]:
         print('Ритма нет: “Пам парам”')
         break
else: print('Ритм есть: “Парам пам-пам”')






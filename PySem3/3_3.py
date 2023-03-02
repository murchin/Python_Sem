# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

text= str(input ('Введите слово на англ или на русск языке:'))
word= text.replace(' ','').upper()


import re
def isCyrillic(word):
	return bool(re.search('[а-яА-Я]', word))

OneE=['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
OneR=['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']

TwoE=['D', 'G']
TwoR=['Д', 'К', 'Л', 'М', 'П', 'У']

ThreeE=['B', 'C', 'M', 'P']
ThreeR= ['Б', 'Г', 'Ё', 'Ь', 'Я']

FourE=['F', 'H', 'V', 'W', 'Y']
FourR=['Й', 'Ы']

FiveE=['K']
FiveR=['Ж', 'З', 'Х', 'Ц', 'Ч']

EightE=['J', 'X']
EightR=['Ш', 'Э', 'Ю']

TenE=['Q', 'Z']
TenR=['Ф', 'Щ', 'Ъ']

counter=0

if isCyrillic(word)==True:
    for i in range(len(word)):
        if word[i] in  OneR:
            counter+=1
        if word[i] in TwoR:
            counter+=2
        if word[i] in ThreeR:
            counter+=3
        if word[i] in FourR:
            counter+=4
        if word[i] in FiveR:
            counter+=5
        if word[i] in EightR:
            counter+=8
        if word[i] in TenR:
            counter+=10
else:
    for i in range(len(word)):
        if word[i] in OneE:
            counter+=1
        if word[i] in TwoE:
            counter+=2
        if word[i] in ThreeE:
            counter+=3
        if word[i] in FourE:
            counter+=4
        if word[i] in FiveE:
            counter+=5
        if word[i] in EightE:
            counter+=8
        if word[i] in TenE:
            counter+=10

print (word.lower())
print (counter,'очков')
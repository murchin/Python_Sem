def get_op():
    print('Введите цифру, соответствующую действию')
    print('1-добавить')
    print('2-показать информацию')
    print('3-удалить')
    print('4-изменить')
    print('5-выход')
    op=int(input(':'))
    return op
#get_op()
def get_data():
    print('Введите новые данные: ')
    name=input('Введите имя: ')
    surname=input('Введите фамилию: ')
    telefon=input('Введите телефон: ')
    data_str=name+" "+surname+" "+telefon+"\n"
    return data_str

def find_person():
    data_str=input('Введите параметр поиска:')
    return data_str



def delete_data():
    data_str=input('Введите характеристику для удаления строки:')
    return data_str
    
def choose_str():        
        answer=int(input('Введите номер строки, которую хотите удалить: '))
        return answer
   

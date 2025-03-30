import os
import re

def get_path(message):
    
    file_path = "";
    data_received = False
    
    print(message)

    while (os.path.exists(file_path) == False or data_received == False):

        file_path = input()
    
        if os.path.exists(file_path):            

            if data_verification(file_path):
                print("!Успешно: файл открыт")
                data_received = True
                return file_path
            else:
                print("!Файл есть, но в данных ошибка, попробуй другой файл")

        else:
            print("!Ошибка, файла нет, попробуй ввести еще раз")


def data_verification(file):
    
    with open(file, encoding='utf-8') as f:
        s = f.read()
    numbers = re.findall(r"(-?\d+\.?\d*)", s)

    only_int  = check_integers_only_in(numbers)

    return only_int and len(numbers)>1

def check_integers_only_in(numbers):
    result = True

    for i in numbers:

        if i.replace('-', '') .isdecimal() == False:
            result = False
    return result

def calculation_min_count_steps(link_file): 
    with open(link_file, encoding='utf-8') as f:
        s = f.read()
    numbers = re.findall(r"(-?\d+\.?\d*)", s)
    
    list_steps =[]
    
    min_num = int(min(numbers))
    max_num = int(max(numbers))
    
    #print(min_num, " ",max_num)

    for i in range(min_num, max_num+1):
        
        current_steps = 0

        for index, other_value in enumerate(numbers):

            current_steps += abs(i-int(other_value))
            
        list_steps.append(current_steps)
        
        #print("шагов до ",i, current_steps)
        
    #print("Результаты ", list_steps)

    ''' #Вариант, когда проверяем только те числа, которые есть в массиве
    for current_i, current_value in enumerate(numbers):
        
        current_steps = 0

        #print(f" Текущий: {current_value}" + "   \nвсе остальные: \n")
        
        for index, other_value in enumerate(numbers):
            if (current_i!=index):
                #print(f" не текущий: {other_value}" )
                current_steps += abs(int(other_value) - int(current_value))
        list_steps.append(current_steps)
    '''

    min_value = min(list_steps)
    
    print("Набор чисел " + str(numbers) +"\n"+ "Минимальное количество ходов, требуемых для приведения всех элементов к одному числу: " + str(min_value))




    
path_file = get_path(">>> Введи путь на файл с массивом целых числе")

calculation_min_count_steps(path_file)




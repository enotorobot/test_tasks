import sys
import os
import re


def data_verification(file):
    
    result = True

    if os.path.exists(file):  

        with open(file, encoding='utf-8') as f:
            s = f.read()
        numbers = re.findall(r"(-?\d+\.?\d*)", s)

        if len(numbers)>1:

            if check_integers_only_in(numbers) == False:
                print('Должны быть только целые числа и без дробной части')
                result = False
        else:
            print('Должно быть больше 1 числа')
            result = False

    else:
        print('Файла не суествует')
        result = False
        
    return result

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

    #print("Набор чисел " + str(numbers) +"\n"+ "Минимальное количество ходов, требуемых для приведения всех элементов к одному числу: " + str(min_value = min(list_steps)))
    print(min(list_steps))



path_file = sys.argv[1:][0]
          
if data_verification(path_file):
    calculation_min_count_steps(path_file)



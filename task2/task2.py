from enum import Enum
import sys
import os
import re


class Data_type(Enum):
    circle = 0
    points = 1

    
def path_verification(paths):
    
    result = True

    if len(paths) == 2:

        for path in paths:
            if os.path.isfile(path) == False:
                result = False
                print("Ошибка файл:", path," не существует")
    else:
        print("Ошибка в количестве переданных имён файлов")
        result = False

    return result


def data_verification(file, data_type):
    
    with open(file, encoding='utf-8') as f:
        s = f.read()
    numbers = re.findall(r"(-?\d+\.?\d*)", s)

    result = False

    if data_type == Data_type.circle:
        
        if len(numbers) == 3:
            check_numbers_in_range (pow(10, -38), pow(10, 38), numbers, 2 )
            result = True

        
        return result
    
    if data_type == Data_type.points:
        
        if (len(numbers) % 2 == 0) and len(numbers)>0 and len(numbers)<=200:
            check_numbers_in_range (pow(10, -38), pow(10, 38), numbers, len(numbers) )
            result = True  
                    
        if  len(numbers)>200:
            print("В файле должно быть до 100 точек")
            
        if (len(numbers) % 2 != 0):
            print("Должны быть пары чисел x и y")
        return  result
    

def check_numbers_in_range(a,b, numbers, check_range):
    #проверка на диапазон, но будем исходить
   
    for i in range(0, check_range):
        
        if  (a<=float(numbers[i])<=b) == False:
            result = False
            print("Координата ", numbers[i] ,"по номеру ", i+1 ," не в диапазоне от ", a ," до ", b)


def calculation_points_position(file_circle, file_points): 

    data_circle = get_circle_from(file_circle)
    
    circle_x      = data_circle[0]
    circle_y      = data_circle[1]
    circle_radius = data_circle[2]

    data_points = get_points_from(file_points)

    for i in range(0, len(data_points), 2):    
        xy = data_points[i:i+2]
        checking_point(float(circle_x), float(circle_y), float(circle_radius), float(xy[0]), float(xy[1]))
        


def get_circle_from(file):
    
    with open(file, encoding='utf-8') as f:
        s = f.read()
        
    numbers = re.findall(r"(-?\d+\.?\d*)", s)

    x = numbers[0]
    y = numbers[1]
    r = numbers[2]

    return [x, y, r];


def get_points_from(file):

    with open(file, encoding='utf-8') as f:
        s = f.read()
    numbers = re.findall(r"(-?\d+\.?\d*)", s)

    return numbers
    

def checking_point(circle_x,circle_y, radius, point_x, point_y):
   
    result = pow(point_x - circle_x, 2) + pow(point_y - circle_y, 2)

    if (result == pow(radius, 2)):
        print("0\n")

    if (result < pow(radius, 2)):
        print("1\n")    

    if (result > pow(radius, 2)):
        print("2\n")



paths = sys.argv[1:]

if path_verification(paths):
    if data_verification(paths[0],Data_type.circle) and data_verification(paths[1],Data_type.points):
        calculation_points_position(paths[0], paths[1])
   

from enum import Enum
import os
import re


class Data_type(Enum):
    circle = 0
    points = 1

    
def get_path(message, data_type):
    
    file_path = "";
    data_received = False
    
    print(message)

    while (os.path.exists(file_path) == False or data_received == False):

        file_path = input()
    
        if os.path.exists(file_path):            

            if data_verification(file_path,data_type):
                print("!Успешно: файл открыт")
                data_received = True
                return file_path
            else:
                print("!Файл есть, но в данных ошибка, попробуй другой файл")

        else:
            print("!Ошибка, файла нет, попробуй ввести еще раз")

def data_verification(file, data_type):
    
    with open(file, encoding='utf-8') as f:
        s = f.read()
    numbers = re.findall(r"(-?\d+\.?\d*)", s)

    result = False

    if data_type == Data_type.circle:
        
        if len(numbers) == 3:
            if check_numbers_in_range (pow(10, -38), pow(10, 38), numbers, 2 ):
                result = True
        
        return result
    
    if data_type == Data_type.points:
        
        if (len(numbers) % 2 == 0) and len(numbers)>0 and len(numbers)<=100:
            if check_numbers_in_range (pow(10, -38), pow(10, 38), numbers, len(numbers) ):
                result = True  
                    
        return  result
    

def check_numbers_in_range(a,b, numbers, check_range):
    
    result = True
   
    for i in range(0, check_range):
        
        if  (a<=float(numbers[i])<=b) == False:
            result = False
            print("Координата ", numbers[i] ,"по номеру ", i+1 ," не в диапазоне от ", a ," до ", b)
    return result

def calculation_points_position(file_circle, file_points): 
    
    data_circle = get_circle_from(file_circle)
    
    circle_x      = data_circle[0]
    circle_y      = data_circle[1]
    circle_radius = data_circle[2]

    data_points = get_points_from(file_points)

    print("Результат вычислений:")

    for i in range(0, len(data_points), 2):    
        xy = data_points[i:i+2]
        checking_point(float(circle_x), float(circle_y), float(circle_radius), float(xy[0]), float(xy[1]))
        
    print("! Конец вычислений ")


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



file_circle = get_path(">>> Введите путь к файлу c данными круга: ", Data_type.circle)
file_points = get_path(">>> Введите путь к файлу c данными точек: ", Data_type.points)

calculation_points_position(file_circle, file_points)




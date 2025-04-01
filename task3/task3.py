import json
import sys
import os

data_tests = {}

def path_verification(paths): #минимальна§ проверка
    
    result = True

    if len(paths) == 3:

        for i in range(2):
            if os.path.isfile(paths[i]) == False:
                result = False
                print("Ошибка файл:", paths[i]," не существует")
    else:
        print("Ошибка в количестве переданных имён файлов")
        result = False

    return result

def report_generation(path_values, path_tests , path_report):
   
    with open(path_tests, 'r') as json_file:
        data_tests = json.load(json_file)

    with open(path_values, 'r') as json_file:
    
        data_value = json.load(json_file)
    
        for element in data_value['values']:
            #print('id: ' + str(element['id']))
            #print('value: ' + str(element['value']))
        
            data_replace_info(data_tests, element['id'] , 'value', element['value'])


    with open(path_report, 'w') as file:
        json.dump(data_tests, file, indent = 4, sort_keys = True)
    #print("Отчет создан")
    
def data_replace_info(data, replace_id_element, replace_val_key, val):
    
    for element in data['tests']:

        if replace_id_element == element["id"]: #нашли элемент с нужным id и перезаписываем
            element[replace_val_key] = val
            break;
        else:                           #ищем вложеные элементы и среди них с нужным id
            nested_search_id(element, replace_id_element, replace_val_key, val)


def nested_search_id(element, replace_id_element, replace_val_key, val):
    
    if 'values' in element:

        for sub_element in element['values']:

            if int(sub_element['id']) == replace_id_element:
                sub_element[replace_val_key] = val
            else:
                nested_search_id(sub_element, replace_id_element, replace_val_key, val)
                
                
paths = sys.argv[1:]

if path_verification(paths):
    report_generation(paths[0], paths[1], paths[2])

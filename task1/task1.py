import sys

def numbers_verification(numbers): #минимальна§ проверка
    
    result = True

    if len(numbers) == 2:
     
        for n in numbers:
            if n.isdecimal() == False:
                print("!Ошибка ввода числа")
                result = False
            else:
                
                if int(n)<1:
                    print("0 не подходит")
                    result = False

    else:
        result = False
        print("Ошибка, передано не 2 значения")
        
    return result

def calculate(n, m):
    
    array = []

    for i in range(1, n+1):
        array.append(i)
    
    #print("Массив для n = "+str(n)+" \n" + str(array) + "...")
    #print("Длина интервала m = "+str(m)+"\n")

    pos_start = 0
    pos_end = (m-1)

    path = str(array[pos_start])

    while (array[pos_end%n] != array[0]):
    
        #print("Интервал:\nИндекc:   "+str(pos_start) +"..." +str(pos_end) +"\nЗначения: ["+ str(array[pos_start%n]) +"]..." +str(array[pos_end%n] )+"\n")

        pos_start = pos_end
        pos_end   = pos_start + (m-1)
    
        path +=str(array[pos_start%n])
    

    #print("Интервал:\nИндекc:   "+str(pos_start) +"..." +str(pos_end) +"\nЗначения: ["+ str(array[pos_start%n]) +"]..." +str(array[pos_end%n] )+"\n")
    print("Полученный путь: "+str(path))


numbers = sys.argv[1:]

if numbers_verification(numbers):
    calculate(int(numbers[0]), int(numbers[1]))

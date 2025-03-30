def get_num(message):
    print(message)
    
    num=-1

    while(num==-1):
        
        num = input()
        
        if(num.isdecimal() == False ):
            
            print("!Ошибка, введите  положительное, целое число")
            num=-1
        else:
            if (int(num) == 0):
                print("!Слишком маленькое число, введите еще раз")
                num=-1
            else:
                return int(num)

def calculate(n, m):
    
    array = []

    for i in range(1, n+1):
        array.append(i)
    
    print("Массив для n = "+str(n)+" \n" + str(array) + "...")
    print("Длина интервала m = "+str(m)+"\n")

    pos_start = 0
    pos_end = (m-1)

    path = str(array[pos_start])

    while (array[pos_end%n] != array[0]):
    
        print("Интервал:\nИндекc:   "+str(pos_start) +"..." +str(pos_end) +"\nЗначения: ["+ str(array[pos_start%n]) +"]..." +str(array[pos_end%n] )+"\n")

        pos_start = pos_end
        pos_end   = pos_start + (m-1)
    
        path +=str(array[pos_start%n])
    

    print("Интервал:\nИндекc:   "+str(pos_start) +"..." +str(pos_end) +"\nЗначения: ["+ str(array[pos_start%n]) +"]..." +str(array[pos_end%n] )+"\n")
    print("Полученный путь: "+str(path))


n = get_num(">>>Задайте длину массива:")
m = get_num(">>>Задайте длину интервала:")

calculate(n, m)


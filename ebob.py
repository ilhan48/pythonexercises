
"""
Kullanıcıdan 2 tane sayı alarak bu 
sayıların en büyük ortak bölenini (EBOB) 
dönen bir tane fonksiyon yazın.
"""

def prime(number):
    if number <= 1:
        print("This primalty of the number cannot be calculated!")
    else:
        for i in range(2,number):
            if (number % i == 0):
                return number
            
        

def ebob(number1,number2):
    listNum1 = {1}
    listNum2 = {1}
    prime(number1)
    for i in range(1,number1):
        if number1 % i == 0:     
            listNum1.add(i)
    prime(number2)
    for i in range(1,number2):
        if number2 % i == 0:     
            listNum2.add(i)
    print(max(listNum1.intersection(listNum2)))
    

ebob(15, 20)





















print("**** WELCOME TO BASİC CALCULATOR ****")
print("\n\n\n")
print("PROCESS:")
print("1-) Addition")
print("2-) Subtraction")
print("3-) Multiplication")
print("4-) Division")
print("5-) Modulus")
print("6-) Exponent")
print("7-) Floor Division")
print("8-) Square root ")
process = int(input("Please select a process: \n\n"))



if (process == 1):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} + {} = {}".format(value1, value2, value1 + value2))
elif (process == 2):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} - {} = {}".format(value1, value2, value1 - value2))
elif (process == 3):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} * {} = {}".format(value1, value2, value1 * value2))
elif (process == 4):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} / {} = {}".format(value1, value2, value1 / value2)) 
elif (process == 5):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} % {} = {}".format(value1, value2, value1 % value2))       
elif (process == 6):
    value1 = int(input("Please enter under value: "))
    value2 = int(input("Please enter top value: "))
    print("{} ** {} = {}".format(value1, value2, value1 ** value2))    
elif (process == 7):
    value1 = int(input("Please enter 1.value: "))
    value2 = int(input("Please enter 2.value: "))
    print("{} // {} = {}".format(value1, value2, value1 // value2))   
elif (process == 8):
    value1 = int(input("Please enter 1.value: "))
    print("{} ** 0.5 = {}".format(value1, value1 ** 0.5))
    

else:
    print("You entered incorrect transaction...\nTry again..5")
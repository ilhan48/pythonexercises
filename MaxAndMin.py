print("*** MAX and MİN CALCULATOR***\n\n")
value1 = int(input("Please enter 1. value: "))
value2 = int(input("Please enter 2. value: "))
value3 = int(input("Please enter 3. value: "))

max = value1
if (value2 > max):
    max = value2
if (value3 > max):
    max = value3 
    print("Max: {}".format(max))
else:
    print("Max: {}".format(max))
    
    
min = value1
if (value2 < min):
    min = value2
if (value3 < min):
    min = value3
    print("Min: {}".format(min))
else:
    print("Min: {}".format(min))
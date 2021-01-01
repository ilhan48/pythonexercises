print("***CHANGE VALUE***")

value1 = int(input("Please enter 1. Value: "))
value2 = int(input("Please enter 2. Value: "))

value1,value2 = value2,value1

print("Value1: {}, Value2: {}".format(value1, value2))
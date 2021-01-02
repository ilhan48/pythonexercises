print("""
*********************************
PERFECT NUMBER CALCULATOR PROGRAM
*********************************
""")


perfectNumber = int(input("Please enter a number: "))
total = 0
for i in range(1,perfectNumber):
    if perfectNumber % i == 0:
        total += i
        if total == perfectNumber:
            print("This number is the perfect number.")
    else:
        print("This number is not the perfect number.")            
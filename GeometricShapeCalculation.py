print("***GEOMETRIC SHAPE CALCULATION PROGRAM***")


print("press 3 for trinagle ")
print("press 4 for quadrilateral ")
shape = int(input("ANSWER: "))

if (shape == 4):
    print("NOTE:The length measure will not be a negative value.")
    a = int(input("Enter a edge: "))
    b = int(input("Enter a edge: "))
    c = int(input("Enter a edge: "))
    d = int(input("Enter a edge: "))
    if (a == b == c == d ):
        print("A square information has been entered.")
    elif (((a == b) and (c == d)) or ((a == c) and (b == d))  or ((a == d) and (b == c))):
        print("A rectangle information has been entered.")
    else:
        print("Ordinary quadrilateral information has been entered.")
elif (shape == 3):
    print("NOTE:The length measure will not be a negative value.")
    x = int(input("Enter a edge: "))
    y = int(input("Enter a edge: "))
    z = int(input("Enter a edge: "))
    if ((x-y)<z):
        print("")
    if (( x + y ) > z ):
        print("The condition of being a triangle is met.")
        if (x == y == z):
            print("\nEquilateral triangle information has been entered.")
        elif ((x == y) or (x == z) or (y  == z)):
            print("Isosceles triangle information has been entered.")
        else:
            print("Scalene triangle information has been entered.")
    else:
        print("The triangle requirement was not met.")


else:
    print("You entered incorrect data! TRY AGAIN...")    
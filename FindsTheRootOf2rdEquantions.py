print("****The program that finds the root of the 2nd degree equations\n\n\n***")


"""
Equation: ax^2 + bx + c

Calculation the Delta: b^2 -4ac

1. root: (-b - delta ** 0.5) / 2a
2. root: (-b + delta ** 0.5) / 2a

"""
a = int(input("\nPlease enter the x^2's constant number: "))
b = int(input("\nPlease enter the x's constant number: "))
c= int(input("\nPlease enter the  constant number: "))

delta = b**2 - (4*a*c)

print("\nThis equation's delta:{}".format(delta))

root1 = (-b - (delta ** 0.5)) / 2 * a
root2 = (-b + (delta ** 0.5)) / 2 * a


print("\n\nThis equantion's 1. root{}".format(root1))
print("\n\nThis equantion's 2. root{}".format(root2))
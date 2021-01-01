print("***Body Mass Calculator***")

"""
Body Mass Formul: Weight / Height(m)* Height(m)
"""

weight = float(input("\n\n\nPlease enter your weight: "))
height = float(input("\nPlease enter your height(m): "))
print("\n\n")
bodyMass = weight / (height*height)

print("Your Body Mass Result: {}\n\n".format(bodyMass))

if (bodyMass < 18.5):
    print("You are weak by standard calculations.")
elif (bodyMass < 25 ):
    print("You are normal by standard calculations.")
elif (bodyMass < 30):
    print("You are owerweight by standart calculations.")
else:
    print("You are obese by standard calculations.")
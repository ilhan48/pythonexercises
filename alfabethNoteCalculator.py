print("***NOTE CALCULATOR***\n")

exam1 = int(input("Please enter EXAM 1: ")) # to effect 30% 
exam2 = int(input("Please enter EXAM 2: ")) # to effect 30%
exam3 = int(input("Please enter EXAM 3: ")) # to effect 40%

note = (exam1 * 0.30) + (exam2 * 0.30) + (exam3 * 0.40)

if (note >=90):
    print("Your Note: AA")
elif (note >=85):
    print("Your Note: BA")
elif (note >=80):
    print("Your Note: BB")
elif (note >=75):
    print("Your Note: CB")
elif (note >=70):
    print("Your Note: CC")
elif (note >=65):
    print("Your Note: DC")
elif (note >=60):
    print("Your Note: DD")
elif (note >=55):
    print("Your Note: FD")
elif (note >=50):
    print("Your Note: FF")
else:
    print("You failed the lesson.")    
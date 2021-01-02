print("""
*******************************)

The multiplication table

*******************************
""")


for i in range(1,10):
    print("***************")
    print("\n{}'s multiplication numberal.\n".format(i))
    for j in range(1,10):
        print(i*j)
    print("\n***************")
print("""
********************
FACTORIAL CALCULATOR 
********************""")

a = 1
b = 1
factorial = []

while True:
    factorial.append(a)
    factorial.append(b)
    
    for i in range(20):
        a,b = b,a+b
        factorial.append(b)
    print(factorial)     
    break   
        
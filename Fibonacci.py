print("""
********************
FİBONACCI CALCULATOR 
********************""")

a = 1
b = 1
fibonacci = []

while True:
    fibonacci.append(a)
    fibonacci.append(b)
    
    for i in range(20):
        a,b = b,a+b
        fibonacci.append(b)
    print(fibonacci)     
    break   
        
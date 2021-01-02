total = 0
q =''

while True:
    
    value = input("Please enter a value: ")
    if (value == 'q'):
        print("Exit program...")
        break
    else:
        total += int(value)
    print("Total: ",total)

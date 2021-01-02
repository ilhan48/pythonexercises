def prime(number):
    if number <= 1:
        print("This primalty of the number cannot be calculated!")
    else:
        for i in range(2,number):
            if (number % i == 0):
                print("This number is not prime.")
                break
            else:
                print("This number is prime.")
                break
        
prime(82)    
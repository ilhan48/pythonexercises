def divisor(number):
    divisors = []
    for i in range(1,number):
        if (number % i == 0):
            divisors.append(i)
    print(divisors)
divisor(8)
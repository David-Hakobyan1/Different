n=int(input("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range(1,n+1):
        factorial = factorial * i
        print (factorial)
    print("factorial " +str(n) + " is " + str(factorial))

def factorial(n):
    if n <= 0:
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial
print(factorial(n))

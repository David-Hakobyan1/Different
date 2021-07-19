def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(10))

fib1 = 1
fib2 = 1
n = int(input("mutq: "))
for i in range(2,n):
    fib1,fib2 = fib2,fib1+fib2
    #print(fib2)

def pow(x,n,i,mult):
    if n == 0:
        return i
    elif n == 1:
        return x
    else:
        y = pow(x,n//2,i,mult)
        y = mult(y,y)
        if n % 2:
            y = mult(x,y)
        return(y)

def identity_matrix(n):
    r = list(range(n))
    return[[1 if i == j else 0 for i in r] for j in r]

def matrix_multiply(a,b):
    bt = list(zip(*b))
    return [[sum(a*b
                for a,b in zip(row_a,col_b))
            for col_b in bt]
            for row_a in a]

def fib(n):
    f = pow([[1,1],[1,0]],n,identity_matrix(2),matrix_multiply)
    return f[0][1]



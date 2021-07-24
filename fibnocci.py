def fib(n):
    a = 0
    b = 1
    if n<0:
        print("INNCORRECT input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        if n in range(2,n):
            c = a+b
            a=b
            b=c
        return b


print(fib(9))
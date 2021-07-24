def table(t):
    for i in range(1, 11):
        print(f'{t} * {i} = {t * i}')



t=int(input("enter the table number: "))
print(table(t))
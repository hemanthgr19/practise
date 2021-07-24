y = int(input("enter the yea : "))
if(y%4)==0:
    if(y%100):
        if(y%400):
            print(f'{y} is a leap year')
        else:
            print(f'{y} is a not leap year')
    else:
        print(f'{y} is a leap year')
else:
    print(f'{y} is not a leap year')
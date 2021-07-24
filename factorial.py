def fun(tea):
    if tea < 0:
        return 0
        #print("0")
    elif tea == 0 or tea == 1:
        return 1
        #print("the value is equal to 0")
    else:
        fact = 1
        while (tea > 0):
            fact *= tea
            tea -= 1
        return fact


tea = 3
print(tea, fun(tea))



#print(n)

def intrest( p,t,r ):

    print(f"the principle amount :{p}")
    print(f"the time period is : {t}")
    print(f"the rate of intrest is : {r}")

    si = p*t*r/100

    print(si)
    return ""


#p,t,r =int(input())
print(intrest(10000,2,3))
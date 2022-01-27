def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
num=int(input("Enter a Number = "))
print("factorial",fact(num))

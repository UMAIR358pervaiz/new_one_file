def odd(x):
    if (x%2!=0):
        return 1
    else:
        return 0
num=int(input("Enter a Number = "))
_odd=odd(num)
if (_odd==1):
    print("Nubmer is odd")
else:
    print("Number is even")

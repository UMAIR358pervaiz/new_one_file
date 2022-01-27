def prime(x):
 if (x<=1):
    print("Number is not Prime nor Composite")
 else: 
    for i in range(2,x):
        if (x%i==0):
            return 0
        else:
            return 1
num=int(input("Enter a Number = "))
_prime=prime(num)
if _prime==0:
    print("Number is Composite")
else:
    print("Number is Prime")

     

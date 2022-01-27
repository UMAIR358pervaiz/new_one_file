def prime(a):
    x=1
    y=2
    while x<=a:
        prime=0
        for i in range (2,y):
            if(y%i==0):
                prime+=1
        if(prime==0):
            print(y)
            x+=1
        y=y+1
num=int(input("Enter a number="))
_prime=prime(num)
print(_prime)
   

def fibo(x):
    if x==0 or x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
fibonacci=[]
for i in range (int(input("Enter a Number="))):
     fibonacci.append(fibo(i))
print(fibonacci)
        

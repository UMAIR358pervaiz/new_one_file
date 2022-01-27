def fibo(x):
    if x==0 or x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
num=int(input("Enter a Number="))
for i in range (num):
     print(fibo(i))
        

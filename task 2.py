def even (x):
    if x%2==0:
        return 1
    else:
        return 0
num=int(input("Enter a Number = "))
_even=even(num)
if _even==1:
    print("Number is Even")
else:
    print("Number is Odd")

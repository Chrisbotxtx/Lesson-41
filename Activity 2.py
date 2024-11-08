def fact(N):
    if N==1:
        return N
    else:
        return N*fact(N-1)
num=int(input("Please enter a number"))

if num<0:
    print("Can't find factorials on numbers less than 0")
elif num==0:
    print("Factorial is 1")
else:
    print("Factorial of",num,"is",fact(num))
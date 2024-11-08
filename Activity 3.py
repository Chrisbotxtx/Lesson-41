
def sum1(a,b):
    return a+b

def Difference(a,b):
    return a-b

def Product(a,b):
    return a*b

def Quotient(a,b):
    return a/b

n1=int(input("Enter first number"))
n2=int(input("Enter Second number"))

print("Sum of {0} and {1} is {2}".format(n1,n2,sum1(n1,n2)))
print("Difference of {0} and {1} is {2}".format(n1,n2,Difference(n1,n2)))
print("Product of {0} and {1} is {2}".format(n1,n2,Product(n1,n2)))
print("Quotient of {0} and {1} is {2}".format(n1,n2,Quotient(n1,n2)))
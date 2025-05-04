def addBinary(a,b):
    num1=int(a,2)
    num2=int(b,2)
    total=num1+num2
    return bin(total)[2:]
print(addBinary("11","1"))
print(addBinary("1010","1011"))
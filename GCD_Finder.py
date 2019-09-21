def gcd(num1,num2):
    if(num2 == 0):
        print(num1)
        return num2
    else:
        gcd(num2,num1%num2)
        return 0

def isPrime(num):
    index = 1
    occurances = 0
    while(index < num):
        if(num%index == 0):
            occurances = occurances + 1
        index = index + 1

    if(occurances > 1):
        return False
    else:
        return True



num1 = int(input("Enter value one to find gcd of :  "))
num2 = int(input("Enter value two to find gcd of :  "))
gcd(num1,num2)

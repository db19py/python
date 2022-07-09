num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    for i in range(num1,num2,-1):
        if i%8==0:
            print(i)
    
else:
    for i in range(num1,num2):
        if i%8==0:
            print(i)

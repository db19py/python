number=int(input("Enter an number:"))
if (number%2 == 0) and (number > 2 and number < 5):
    print("Not Weird")
elif (number%2 == 0) and (number > 6 and number < 20):
    print("Weird")
elif (number%2 == 0) and (number > 20):
    print("Not Weird")
else:
    print("Weird")

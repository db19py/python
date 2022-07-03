mark=int(input("Enter your mark"))
if (mark > 0 and mark < 100):
    if (mark >= 90 and mark <=100):
        print("Pass")
        print("A")
    elif (mark >= 80 and mark <=89):
        print("Pass")
        print("B")
    elif (mark >= 70 and mark <=79):
        print("Pass")
        print("C")
    elif (mark >= 60 and mark <=69):
        print("Pass")
        print("D")
    elif (mark >= 50 and mark <=59):
        print("Pass")
        print("E")
    else:
        print("Fail")
else:
    print("Invalid Mark")

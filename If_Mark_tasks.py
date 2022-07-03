m1=float(input("enter the mark1:"))
m2=float(input("enter the mark2:"))
m3=float(input("enter the mark3:"))
if (m1 > 0 and m1 <100) and (m2 > 0 and m2 <100) and (m3 > 0 and m3 <100):
    Total=int((m1+m2+m3)/3)
    print(Total)
    if Total > 90:
            print("GradeA")
    elif Total > 75:
            print("GradeB")
    elif Total > 50:
            print("GradeC")
    else:
            print("GradeD")
else:
    print("Numbers are not in the range")


    
    

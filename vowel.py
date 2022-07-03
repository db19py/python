string=input("Enter a string")
middle_str=len(string)//2
print(string[middle_str])
if (string[middle_str]=='a' or string[middle_str]=='e' or string[middle_str]=='i' or string[middle_str]=='o' or string[middle_str]=='u'):
    print("vowel")
else:
    print("not a vowel")

'''
#collect two strings from user

string1: python
String2: java

output ===> jythonpava64hv

string1: maths
string2: science

output ===> sathsmcience57te
'''

string1='python'
string2='java'

a=string1[0]
b=string2[0]

length1=len(string1)
length2=len(string2)

middlechar1= length1//2
middlechar2= length2//2

print(b+string1[1::]+a+string2[1::]+str(length1)+str(length2)+string1[middlechar1]+string2[middlechar2])

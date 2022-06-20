'''
collect three strings from user  name<space>float

string1: "ravi 10.30"  
string2: "meghala 12.19"
string3: "Gokul 20.20"

split + indexing

10.30 + 12.19 + 20.20 ===> output ===> add it 42.69
'''

string1=input('Enter the name<space>float:')
string2=input('Enter the name<space>float:')
string3=input('Enter the name<space>float:')
s1=string1.split()
s2=string2.split()
s3=string3.split()
#a=s1[1]
#b=s2[1]
#c=s3[1]
#d=float(a)
#e=float(b)
#f=float(c)
print(float(s1[1])+float(s2[1])+float(s3[1]))



'''
Collect two strings from user

string1: wikipedia
string2: typescript

output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
(ord , chr)
'''

string1='wikipedia'
string2='typescript'
middle_char1=len(string1)//2
middle_char2=len(string2)//2
print(ord(string1[middle_char1])+ord(string2[middle_char2]))

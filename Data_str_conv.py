'''
Task7:

Covert below two lists in to a dictionary

[1,2,3,4,5]
["python","cpp","c","java","php"]


Task8:

Convert below set in to a list

{5,4,3,6,2,7,1}

Task9:

Remove duplicates from below list

[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]


Task10:

Convert below one to tuple

[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
'''
Li1=[1,2,3,4,5]
Li2=["python","cpp","c","java","php"]
print(dict(zip(Li1,Li2)))
set1={5,4,3,6,2,7,1}
print(list(set1))
list1=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(list(set(list1)))
print(tuple(list1))


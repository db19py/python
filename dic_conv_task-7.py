'''Covert below two lists in to a dictionary

[1,2,3,4,5]
["python","cpp","c","java","php"]'''

list1=[1,2,3,4,5]
list2=["python","cpp","c","java","php"]
print(dict(zip(list1,list2)))


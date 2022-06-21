a=[]
#a=list[]
b=a+[5,6,7,8]
c=b+[8,9,1,5,6,7,8,1]
print(c)
count_lst=c.count(8)
print("occurance of 8:",count_lst)
mean=sum(c)/len(c)
print("mean of the list:",mean)
print(sum(c)+ min(c) + max(c))
d=set(c)
print(d)
e=tuple(d)
print(e)

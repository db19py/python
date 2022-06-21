a=[3,1,2]
b=[4,5,6,7]
a.sort()
median1=len(a)//2
print(a[median1])
b.sort()
median2=len(b)//2
print((b[median2] + b[median2 -1])/2)

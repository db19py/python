a=[-1, -7,8,10,20,21,17,28,-3,0,0,]
pos=[]
neg=[]
z=[]
for i in a:
    if i<0:
        neg.append(i)
    elif i==0:
        z.append(i)
    else:
        pos.append(i)
print("+ve list:",pos)
print("-ve list:",neg)       
print("zero list:",z) 

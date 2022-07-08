Li1 = [3,4,5,2,7,8,9,10]
odd=[]
even=[]
for i in Li1:
    if i%2!=0:
        odd.append(i)        
    elif i%2==0:
        even.append(i)
print("odd list:",odd)
print("Even list:",even)

dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#print(type(dict1))
#Extract "bobtn" from above dictionary
print(dict1[3][0][0:9:2])
#Extract "arbeg" from above dictionary
print(dict1[3][-1][:-6:-1])
#print all keys in dictionary and convert it into tuple
print(tuple(dict1.keys()))
#Find the average of all numbers available under key "2"
print((dict1[2][0]+dict1[2][1]+dict1[2][2])/len(dict1[2]))


set1=set()
set2=set()
set3={7,8,9,1,2,3,4,5,0}
set4={4,5,6,0}
set1.update(set3)
set2.update(set4)
print(set1,set2)
print(set2.issubset(set1))
common_set=set1.intersection(set2)
print(common_set)
set1.discard(0)
print(set1)
set2.discard(0)
print(set2)
set1.remove(8)
print(set1)
print (set(list(set1) + list(set2)))



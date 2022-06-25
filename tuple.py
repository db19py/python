tupl1=(1,4,5,6,7,8)
tupl2=(5,6,7,8,9)
common_element = set(tupl1)&set(tupl2)  #& won't allow in tuple
print(common_element)
concat=tupl1+tupl2
print(set(concat))
print(concat.index(9))
print(concat*3)

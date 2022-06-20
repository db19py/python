'''
collect one string from user:

string: computer
output: c6r

string: mathematics
output: m9s
'''

string='computer'
length=len(string[1:-1:1])
print(string[0]+str(length)+string[-1])

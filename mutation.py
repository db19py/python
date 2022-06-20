'''
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
'''

s = 'abracadabra'
l=list(s)
l[5]='k'
print("".join(l))


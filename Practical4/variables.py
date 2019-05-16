
#Created on Wed Mar 13 09:29:01 2019

#@author: 11601

a=812
b=812812
print('''
a=812
b=812812
''')
print('can b be divided by 7?-',b%7 == 0)
c=b/7
d=c/11
e=d/13
print('a =',a,' b =',b)
if e < a:
    print('a is greater than e')
elif e == a:
    print('a is equal to e')
else:
    print('e is greater than a')
print(' ')

X=(a==b)
Y=(a==e)
Z=(X and not Y)or(Y and not X)
W=(X!=Y)

print('X is',X,', Y is',Y)
print('either X or Y (but not both) is true is-',Z)
print('more elegant solution of Zhiwen is-',W)
print('is the Z and W always the same?-',Z==W)



import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from itertools import combinations

d0 = {1:1,2:2,3:3,4:4}
print(d0)
d01 = {'1','2','3','4'}
print(type(d01))
d02 = dict()




d1 = defaultdict(int)
print(d1['a']+1)

C = np.zeros((3,4))
C[2][3] +=1
print(C[2][3])

N = dict()
print(type(N))

k={}
s = [('Tom', 5), ('Jone', 2), ('Susan', 4), ('Tom', 4), ('Tom', 1)]
for i,j in s:
    if i not in k.keys():#注意不能写成 if not k[i],因为其返回值不是None,而是error
        l=[]
        l.append(j)
        k[i]=l
    else:
        k[i].append(j)
print(k)



d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['a'] = 4
d['a'] = 5
d['b'] = 7
d['e'] = 9

print(d)

dd = {'A':{'a','b','d'},'B':{'a','c'}}
for x,y in dd.items():
    for z in y:
        print(z)


list03 = [['a','1'],['b','2'],['a','3']]
list08 = dict()
list08[('x','y')] = 100
print(dict(list08))

train = []
train.append(['1','1'])
train.append(['2','2'])
train.append(['3','3'])
plt.plot(train)
plt.show()
print('####################')
print(train[0])
for u,i in train:
    print(u)
print(dict(train).items())

print('@@@@@@@@@@@@@@@@@@@@@@@')
list02 = [1,2,3,4,5,6]
print(list(combinations(list02,2)))

import itertools
print(list(itertools.permutations(list02,2)))


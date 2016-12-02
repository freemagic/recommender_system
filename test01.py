import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import sparse
from collections import defaultdict
from modelTest import abc

a = np.zeros(1000)
a[400:600] = -1

b = sp.fft(a)
#plt.plot(b)
#plt.show()

ddict = defaultdict(int)        #构造初始值为整型的字典


list = [(1,2),(2,3),(3,4)]
for u,v in list:
    pass
    #print(u+v)


m = set()
m.add(1)
m.add(2)
m.add(3)
m.add(4)

n = set()
n.add(2)
n.add(4)
n.add(6)
x = set()
y = set()
for i in (m & n):
    print(i)

item_users = {'1':{'234','463','3478','908'},'3':{'236','658',''}}

abc()
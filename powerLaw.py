import matplotlib.pyplot as plt

data = []
for line in open(r'E:\PycharmProjects\recommender_system\data\ratings.dat'):
    user,item,rating,ts = line.split('::')
    data.append([user,item])

U = dict()
I = dict()
for u,i in data:
    if u not in U.keys():
        U[u] = 1
    else:
        u_value = int(U.get(u))
        U[u] = u_value+1
    if i not in I.keys():
        I[i] = 1
    else:
        i_value = int(I.get(i))
        I[i] = i_value+1
print(len(U))
print(len(I))

#plt.plot(U)
#plt.show()


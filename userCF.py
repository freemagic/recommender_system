#coding = UTF-8
#Create 2016-10-18

#这里利用原始数据进行处理，没有把切分数据写入本地文件再读取

import fileinput
import random
import math
import numpy as np

#提取数据集中的用户ID和电影ID，以[user,item]的形式组成列表
dataset = []
for line in open(r'/home/spark/PycharmProjects/recommender_system/data\ratings.dat'):
    user,item,rating,ts = line.split("::")
    dataset.append((user,item))

#划分数据集，把数据集划分为M份，其中一份作为测试集
def splitData(data,M,k,seed):
    print('正在进行数据划分......')
    test = []
    train = []
    random.seed(seed)
    for user,item in data:
        if random.randint(1,M) == k:
            test.append((user,item))
        else:
            train.append((user,item))
    print(len(train))
    print(len(test))
    print('WOW! 数据划分完成！')
    return train,test

#得到用户-物品列表
def getUIList(train):
    # build inverse table for item_users
    user_items = dict()
    for u,i in train:
        if u not in user_items:
            user_items[u] = set()
        user_items[u].add(i)
    return user_items

#得到物品-用户倒排表
def getIUList(train):
    item_users = dict()
    for u,i in train:
        if i not in item_users:
            item_users[i] = set()
        item_users[i].add(u)
    return item_users

#计算用户的相似度
def userSimilarity(train):
    print('正在计算用户间的相似度......')
    #得到用户-物品列表
    user_items = getUIList(train)
    #calculate co-rated items between users
    C = np.zeros((6040,6040))
    N = np.zeros(6040)
    for u,items in user_items.items():
        N[int(u)-1] += len(user_items[u])
        for v,items in user_items.items():
            if u != v:
                C[int(u)-1][int(v)-1] += len(user_items[u] & user_items[v])

    #calculate final similarity matrix W
    W = np.zeros((6040,6040))
    for i in range(6040):
        for j in range(6040):
            if C[i][j] != 0:
                W[i][j] = C[i][j] / math.sqrt(N[i] * N[j])
    print('Wonderful! 相似度计算完成！')
    return W

def recommend(train,W,k):
    print('正在计算用户对物品的兴趣度......')
    #得到物品-用户倒排表
    item_users = getIUList(train)
    #获取各个用户最相似的k个用户集合
    S = dict()                        #S为以用户号为键，以与该用户最相似的k个用户的集合为值得字典
    P = np.zeros((6040,3952))         #用户对物品的兴趣度矩阵
    WS = np.argsort(-W,axis=1)+1      #对矩阵W按行将序排序，得到排序后(W未变化)下标对应的矩阵,对下表矩阵全部加1得到用户号，对应上面用户号减1的操作
    for u in np.arange(6040):
        #列表WS[u,0:k]的元素是整型，利用map函数将其每个元素转为字符型，map返回的值是一个对象，利用list函数将其再转化为列表，最后将列表转为集合
        S[u] = set(list(map(str,WS[u,0:k])))
        for i in item_users.keys():
            for uki in (S[u] & item_users[i]):       #uki为与用户u相似的k个用户同时又对物品(i+1)有过行为的用户集合，其中集合users元素为字符型
                P[u][int(i)-1] += W[u][int(uki)-1]
    print('Good! 用户对物品相似度计算完成！')
    return np.argsort(-P,axis=1)        #对用户-物品兴趣度矩阵按行进行将序排序后的下标矩阵


def getRecommendation(pui,train,Num):
    print('正在获取推荐列表......')
    rank = dict()
    user_items = getUIList(train)
    for u in user_items.keys():
        k = 0
        if u not in rank:
            rank[u] = set()
        for i in pui[int(u)-1]:
            if str(i+1) not in user_items[u] and k < Num:
                k += 1
                rank[u].add(str(i+1))
    print('Yes! 推荐列表获取完成！')
    return rank

#计算召回率
def recall(rank,test_user_items):
    hit = 0
    all = 0
    for u in test_user_items:
        hit += len(rank[u] & test_user_items[u])
        all += len(test_user_items[u])
    return hit/(all*1.0)

#计算准确率
def precision(rank,Num):
    hit = 0
    all = 0
    for u in test_user_items:
        hit += len(rank[u] & test_user_items[u])
        all += Num
    return hit/(all*1.0)

#计算覆盖率
def coonverge(train,test,N):
    recommend_items = set()
    all_items = set()
    for user in dict(train).keys():
        for item in train[user].keys():
            all_items.add(item)
    rank = getRecommendation(user,N)
    for item,pui in rank:
        recommend_items.add(item)
    return len(recommend_items) / (len(all_items) * 1.0)

#计算F1值
def f1Value(recall,precision):
    F1 = 2 * recall * precision / (recall + precision)
    return F1

if __name__ == '__main__':
    N = 10;
    train,test = splitData(dataset,8,1,1)
    W = userSimilarity(train)
    P = recommend(train,W,80)
    rank = getRecommendation(P,train,N)
    test_user_items = getUIList(test)
    rc = recall(rank,test_user_items)
    pc = precision(rank,N)
    F1 = f1Value(rc,pc)
    print("召回率：%.2f%%" % (rc*100))
    print("准确率：%.2f%%" % (pc*100))
    print("F1值：%.2f" % F1)
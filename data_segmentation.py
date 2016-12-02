#coding = UTF-8
#Create 2016-10-18

#该文件只是切分数据集，分为训练集和测试集，并写到本地文件

import fileinput
import random

#提取数据集中的用户ID和电影ID，以[user,item]的形式组成列表,并把数据写到本地文件

file_all = open(r'E:\PycharmProjects\recommender_system\data\dataset.txt','w')
file_train = open(r'E:\PycharmProjects\recommender_system\data\train.txt','w')
file_test = open(r'E:\PycharmProjects\recommender_system\data\test.txt','w')

dataset = []
for line in open(r'E:\PycharmProjects\recommender_system\data\ratings.dat'):
    user,item,rating,ts = line.split("::")
    dataset.append([user,item])
    file_all.write(user+':'+item+'\n')

#划分数据集，把数据集划分为M份，其中一份作为测试集，把训练集和测试集均写到本地文件

def splitData(data,M,k,seed):
    test = []
    train = []
    random.seed(seed)
    for user,item in data:
        if random.randint(0,M) == k:
            test.append([user,item])
            file_test.write(user+':'+item+'\n')
        else:
            train.append([user,item])
            file_train.write(user+':'+item+'\n')
    #print(train.__len__())
    #print(test.__len__())
    return train,test

#调用切分函数
splitData(dataset,8,7,1)
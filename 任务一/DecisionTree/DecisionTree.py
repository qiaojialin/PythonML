# -*- coding: utf-8 -*-
import numpy as np
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer

''''' 数据读入 '''
data = []
labels = []
with open(r"C:\Users\Administrator\Desktop\数据仓库第二次作业2016\任务一\adult.dataset.txt") as file:
    for line in file:
        tokens = line.strip().split(', ')
        data.append([str(tk) for tk in tokens[:-1]])
        labels.append(tokens[-1])
data.pop(-1)
labels.pop(-1)

x = np.array(data)
labels = np.array(labels)
y = np.zeros(labels.shape)

''''' 标签转换为0/1 '''
y[labels == '>50K'] = 1

''''' 拆分训练数据与测试数据 '''
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = x
y_train = y



data = []
labels = []
with open(r"C:\Users\Administrator\Desktop\数据仓库第二次作业2016\任务一\adult.test.txt") as file:
    for line in file:
        tokens = line.strip().split(', ')
        data.append([str(tk) for tk in tokens[:-1]])
        labels.append(tokens[-1])
data.pop(-1)
labels.pop(-1)

x = np.array(data)
labels = np.array(labels)
y = np.zeros(labels.shape)

''''' 标签转换为0/1 '''
y[labels == '>50K.'] = 1

x_test = x
y_test = y

vec = DictVectorizer()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)

score = clf.score(x_test, y_test)

with open("文件名称.dot", 'w') as f:
  f = tree.export_graphviz(clf, out_file=f, feature_names=vec.get_feature_names())

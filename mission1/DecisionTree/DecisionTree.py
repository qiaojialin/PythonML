# -*- coding: utf-8 -*-
import numpy as np
from sklearn import tree


attr1 = ['?', 'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
attr3 = ['?', 'Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
attr5 = ['?', 'Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
attr6 = ['?', 'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
attr7 = ['?', 'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
attr8 = ['?', 'White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
attr9 = ['?', 'Female', 'Male']
attr13 = ['?', 'United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']


''''' 数据读入 '''
datas = []
labels = []

with open(r"../../dataset/data1/adult.data.txt") as file:
    for line in file:
        tokens = line.strip().split(', ')
        if len(tokens) < 14:
            continue
        labels.append(tokens[-1])
        data = [str(tk) for tk in tokens[:-1]]

        data[0] = int(data[0])
        data[1] = attr1.index(data[1])
        data[2] = int(data[2])
        data[3] = attr3.index(data[3])
        data[4] = int(data[4])
        data[5] = attr5.index(data[5])
        data[6] = attr6.index(data[6])
        data[7] = attr7.index(data[7])
        data[8] = attr8.index(data[8])
        data[9] = attr9.index(data[9])
        data[10] = int(data[10])
        data[11] = int(data[11])
        data[12] = int(data[12])
        data[13] = attr13.index(data[13])
        datas.append(data)

x = np.array(datas)
labels = np.array(labels)
y = np.zeros(labels.shape)

''''' 标签转换为0/1 '''
y[labels == '>50K'] = 1

''''' 拆分训练数据与测试数据 '''
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = x
y_train = y


datas = []
labels = []
with open(r"../../dataset/data1/adult.test.txt") as file:
    for line in file:
        tokens = line.strip().split(', ')
        if len(tokens) < 14:
            continue
        labels.append(tokens[-1])
        data = [str(tk) for tk in tokens[:-1]]

        data[0] = int(data[0])
        data[1] = attr1.index(data[1])
        data[2] = int(data[2])
        data[3] = attr3.index(data[3])
        data[4] = int(data[4])
        data[5] = attr5.index(data[5])
        data[6] = attr6.index(data[6])
        data[7] = attr7.index(data[7])
        data[8] = attr8.index(data[8])
        data[9] = attr9.index(data[9])
        data[10] = int(data[10])
        data[11] = int(data[11])
        data[12] = int(data[12])
        data[13] = attr13.index(data[13])
        datas.append(data)

x = np.array(datas)
labels = np.array(labels)
y = np.zeros(labels.shape)

''''' 标签转换为0/1 '''
y[labels == '>50K.'] = 1

x_test = x
y_test = y


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)


y_predict = clf.predict(x_test)
total = len(y_test)
right = 0
false = 0
for i, val in enumerate(y_predict):
    if val == y_test[i]:
        right += 1
    else:
        false += 1

print 'total:', total
print 'right: ', right
print "right rate: ", float(right)/float(total)*100, "%"
print 'false: ', false
print 'false rate: ', float(false)/float(total)*100, "%"

# import pydotplus
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf(r"tree.pdf")
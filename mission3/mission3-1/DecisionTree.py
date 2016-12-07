# -*- coding: utf-8 -*-
import ReadData
import numpy as np
from sklearn import tree

train_path = r"../../dataset/data3/train/"
x_train, y_train = ReadData.read1(train_path)
print x_train.shape

test_path = r"../../dataset/data3/test/"
x_test, y_test = ReadData.read1(test_path)
print np.unique(y_test)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)

score = clf.score(x_test,y_test)

print "score: ",score

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

'''import pydotplus
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf(r"tree.pdf")

print "done!!!"'''
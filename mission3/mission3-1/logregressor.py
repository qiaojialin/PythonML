#####44dimension best
from numpy import *
from sklearn.datasets import load_iris     # import datasets
# import the LogisticRegression
from sklearn.linear_model import LogisticRegression
import numpy as np
import ReadData

train_path = r"../../dataset/data3/train/"
x_train, y_train = ReadData.read1(train_path, 52)

test_path = r"../../dataset/data3/test/"
x_test, y_test = ReadData.read1(test_path, 52)
print np.unique(y_test)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)

y_predict = classifier.predict(x_test)

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
print "right rate: ", float(right) / float(total) * 100, "%"
print 'false: ', false
print 'false rate: ', float(false) / float(total) * 100, "%"

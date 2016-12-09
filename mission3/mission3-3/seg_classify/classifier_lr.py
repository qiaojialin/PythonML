# 44dimension best
from numpy import *
from sklearn.datasets import load_iris     # import datasets
# import the LogisticRegression
from sklearn.linear_model import LogisticRegression
import numpy as np
import ReadData
import breakpoints

train_path = r"../../../dataset/data3/train/"
x_train, y_train = ReadData.read1(train_path, 52)

test_name = r"../../../dataset/data3/test/13.csv"
x_test, y_test = ReadData.read2(test_name)
print np.unique(y_test)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)

breakpoints = breakpoints.breakpoints(x_test,7)
start = 0
end = 0
total = 0
right = 0
false = 0
for i in breakpoints:
	if i == 0:
		start = i
		end = start
		continue
	else:
		start = end
		end = i
		x_data = x_test[start:end]
		y_data = y_test[start:end]
		if end - start < 52:
			continue
		x, y = ReadData.seqAnalysis(x_data, y_data, 52)
		print "x_data.shape: ", x_data.shape
		print "x.shape: ", x.shape
		y_predict = classifier.predict(x)
		print "y_test: ", y_data[1]
		total_temp = y.shape[0]
		right_temp = 0
		false_temp = 0
		for i, val in enumerate(y_predict):
			if val == y[i]:
				right_temp += 1
			else:
				false_temp += 1
		print 'total_temp:', total_temp
		print 'right_temp: ', right_temp
		print "right rate: ", float(right_temp) / float(total_temp) * 100, "%"
		print 'false_temp: ', false_temp
		print 'false rate: ', float(false_temp) / float(total_temp) * 100, "%"
		total += total_temp
		right += right_temp
		false += false_temp

print 'total:', total
print 'right: ', right
print "right rate: ", float(right) / float(total) * 100, "%"
print 'false: ', false
print 'false rate: ', float(false) / float(total) * 100, "%"

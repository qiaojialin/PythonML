#####40dimension best
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestClassifier  
import numpy as np  
import ReadData
import matplotlib.pyplot as plt
   
train_path = r"../../../dataset/data3/train/"
x_train, y_train = ReadData.read1(train_path, 52, 1)

test_path = r"../../../dataset/data3/test/"
x_test, y_test = ReadData.read1(test_path, 52, 0)
print np.unique(y_test)


rfc = RandomForestClassifier()  
rfc.fit(x_train,y_train)

score = rfc.score(x_train,y_train)
print "score_train: ", score

x_test = ReadData.seqAnalysis(x_test, 52)
y_predict = rfc.predict(x_test)
total = len(y_test)
right = 0
false = 0
for i, val in enumerate(y_predict):
	for j in range(52):
		if val == y_test[52*i+j]:
			right += 1
		else:
			false += 1



for i, val in enumerate(y_predict):
	temp = np.ones((52,1))
	temp = val*temp
	if i == 0:
		Y1 = temp
	else:
		Y1 = np.vstack((Y1,temp))
	
Y1 = Y1.T
print "Y1[0].shape: ", Y1[0].shape
X1 = range(0, Y1[0].shape[0])
Fig1 = plt.figure(figsize=(8,4))                      # Create a `figure' instance
Ax1 = Fig1.add_subplot(211)               # Create a `axes' instance in the figure
Ax1.plot(X1, Y1[0])
Ax2 = Fig1.add_subplot(212)
Ax2.plot(X1, y_test[0:Y1[0].shape[0]])
Fig1.savefig("comprerfc.pdf")



print 'total:', total
print 'right: ', right
print "right rate: ", float(right)/float(total)*100, "%"
print 'false: ', false
print 'false rate: ', float(false)/float(total)*100, "%"
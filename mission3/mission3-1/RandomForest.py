#####40dimension best
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestClassifier  
import numpy as np  
import ReadData
   
train_path = r"../../dataset/data3/train/"
x_train, y_train = ReadData.read1(train_path, 52)

test_path = r"../../dataset/data3/test/"
x_test, y_test = ReadData.read1(test_path,52)
print np.unique(y_test)

train_filename = r"../../data/df_train.csv"
#x_train, y_train = ReadData.read2(train_filename)

test_filename = r"../../data/df_test.csv"
#x_test, y_test = ReadData.read2(test_filename)


rfc = RandomForestClassifier()  
rfc.fit(x_train,y_train)

score = rfc.score(x_train,y_train)
print "score_train: ", score
score = rfc.score(x_test,y_test)
print "score_test: ",score


y_predict = rfc.predict(x_test)
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
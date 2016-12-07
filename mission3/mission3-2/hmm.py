# _*_ coding:utf-8 _*_
# __author__='dragon'
"""
test HMM

"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
import ReadData

test_path = r"../../dataset/data3/temp/"
x_test, y_test = ReadData.read1(test_path)
print np.unique(y_test)
n_states = (np.unique(y_test)).shape[0]

#构建了一个MultinomialHMM模型，这模型包括开始的转移概率，隐含间的转移矩阵A（transmat），隐含层到可视层的混淆矩阵emissionprob，下面是参数初始化
model = GaussianHMM(n_components = n_states)
model = model.fit(x_test, lengths = )
y_predict = model.predict(x_test)

X1 = range(0, x_test.shape[0])
Y1 = y_test # y = x^2
Y2 = y_predict
#X2 = [0, 1]
#Y2 = [0, 1]  # y = x
Fig = plt.figure(figsize=(8,4))                      # Create a `figure' instance
Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
Ax.plot(X1, Y1)
Fig2 = plt.figure(figsize=(8,4))
Bx = Fig2.add_subplot(111)
Bx.plot(X1, Y2)                 # Create a Line2D instance in the axes
Fig.show()
Fig.savefig("test.pdf")
Fig2.show()
Fig2.savefig("predict.pdf")


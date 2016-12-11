# _*_ coding:utf-8 _*_
# __author__='dragon'
"""
test HMM

"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn import hmm
import ReadData
from scipy import signal
import math

def fft_convolve(a,b):
    n = len(a)+len(b)-1
    N = 2**(int(np.log2(n))+1)
    A = np.fft.fft(a, N)
    B = np.fft.fft(b, N)
    return np.fft.ifft(A*B)[:n]

test_path = r"../../../dataset/data3/temp/"
x_test, y_test = ReadData.read1(test_path)
print np.unique(y_test)
n_states = (np.unique(y_test)).shape[0]
###filter input
X = x_test.T
print"x.shape: ", X.shape
b,a=signal.iirdesign(0.001, 0.002, 1, 40, 0, "cheby1")
x_data0 = signal.filtfilt(b, a, X[0])
x_data1 = signal.filtfilt(b, a, X[1])
x_data2 = signal.filtfilt(b, a, X[2])
temp = np.vstack((x_data0,x_data1))
x_data = np.vstack((temp,x_data2))

x_data = x_data.T

print "x_data.shape: ", x_data.shape

model = hmm.GaussianHMM(n_components = n_states)
model1 = model.fit(x_data)
y_predict1 = model.predict(x_data)

model2 = model.fit(x_test)
y_predict2 = model2.predict(x_test)

X_ = range(0, x_test.shape[0])
Y_ = y_test 
temp = 0
result_test = []
for i in range(Y_.shape[0]):
	if Y_[i] == temp:
		continue
	result_test.append(i)
	temp = Y_[i]
print"result_test: ", result_test


b,a=signal.iirdesign(0.0005, 0.001, 1, 40, 0, "cheby1")
Y = signal.filtfilt(b, a, y_predict1)
y_max = float(Y.max())
y_min = float(Y.min())
step = (y_max - y_min)/7.0
#print"max, min, step: ", y_max, y_min, step
Y1 = []
for y1 in Y:
	y = math.floor((y1 - y_min)/step)
	Y1.append(y)
Y1 = np.array(Y1)

Y = signal.filtfilt(b, a, y_predict2)
y_max = float(Y.max())
y_min = float(Y.min())
step = (y_max - y_min)/7.0
#print"max, min, step: ", y_max, y_min, step
Y2 = []
for y2 in Y:
	y = math.floor((y2 - y_min)/step)
	Y2.append(y)
Y2 = np.array(Y2)

temp = 0
result_predict = []
for i in range(Y1.shape[0]):
	if Y1[i] == temp:
		continue
	result_predict.append(i)
	temp = Y1[i]
print"result_predict: ", result_predict

Fig1 = plt.figure(figsize=(8,4))                      # Create a `figure' instance
Ax1 = Fig1.add_subplot(311)               # Create a `axes' instance in the figure
Ax1.plot(X_, Y_)
Ax2 = Fig1.add_subplot(312)               # Create a `axes' instance in the figure
Ax2.plot(X_, y_predict1)
Ax3 = Fig1.add_subplot(313)               # Create a `axes' instance in the figure
Ax3.plot(X_, Y1)
Fig2 = plt.figure(figsize=(8,4))
Bx1 = Fig2.add_subplot(311)               # Create a `axes' instance in the figure
Bx1.plot(X_, Y_)
Bx2 = Fig2.add_subplot(312)               # Create a `axes' instance in the figure
Bx2.plot(X_, y_predict2)
Bx3 = Fig2.add_subplot(313)               # Create a `axes' instance in the figure
Bx3.plot(X_, Y2)
Fig3 = plt.figure(figsize=(8,4))
Cx1 = Fig3.add_subplot(211)
Cx1.plot(range(0, Y_.shape[0]), X[2])
Cx2 = Fig3.add_subplot(212)
Cx2.plot(range(0, Y_.shape[0]), x_data2)
Fig4 = plt.figure(figsize=(8,4))
Dx = Fig4.add_subplot(111)
Dx.plot(range(0, Y_.shape[0]), Y2)                # Create a Line2D instance in the axes
Fig1.savefig("filtedDataResultCompare.pdf")
Fig2.savefig("unfiltedDataResultCompare.pdf")
Fig3.savefig("datacompare.pdf")
Fig4.savefig("predictfilt.pdf")


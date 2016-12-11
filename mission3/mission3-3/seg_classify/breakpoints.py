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


def fft_convolve(a, b):
    n = len(a) + len(b) - 1
    N = 2**(int(np.log2(n)) + 1)
    A = np.fft.fft(a, N)
    B = np.fft.fft(b, N)
    return np.fft.ifft(A * B)[:n]


def breakpoints(data, states):
    n_states = states
    X = data.T
    print"x.shape: ", X.shape
    b, a = signal.iirdesign(0.001, 0.002, 1, 40, 0, "cheby1")
    x_data0 = signal.filtfilt(b, a, X[0])
    x_data1 = signal.filtfilt(b, a, X[1])
    x_data2 = signal.filtfilt(b, a, X[2])
    temp = np.vstack((x_data0, x_data1))
    x_data = np.vstack((temp, x_data2))
    x_data = x_data.T
    print "x_data.shape: ", x_data.shape
    model = hmm.GaussianHMM(n_components=n_states)
    model = model.fit(x_data)
    y_predict = model.predict(x_data)

    b, a = signal.iirdesign(0.0005, 0.001, 1, 40, 0, "cheby1")
    Y = signal.filtfilt(b, a, y_predict)
    y_max = float(Y.max())
    y_min = float(Y.min())
    step = (y_max - y_min) / float(states)
    # print"max, min, step: ", y_max, y_min, step
    Y3 = []
    for y3 in Y:
        y = math.floor((y3 - y_min) / step)
        Y3.append(y)
    Y3 = np.array(Y3)
    temp = 0
    result_predict = []
    for i in range(y_predict.shape[0]):
        if y_predict[i] == temp:
            continue
        result_predict.append(i)
        temp = y_predict[i]
    print"result_predict: ", result_predict
    
    return result_predict

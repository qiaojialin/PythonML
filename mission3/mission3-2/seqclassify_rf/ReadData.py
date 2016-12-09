# -*- coding: utf-8 -*-
import numpy as np
import glob
import csv
from itertools import islice 
import math

def autocorrelation(x,lags):#计算lags阶以内的自相关系数，返回lags个值，分别计算序列均值，标准差
    n = len(x)
    x = np.array(x)
    result = [np.correlate(x[i:]-x[i:].mean(),x[:n-i]-x[:n-i].mean())[0]\
        /(x[i:].std()*x[:n-i].std()*(n-i)) \
        for i in range(1,lags+1)]
    return result


def read1(path, length, flag):

    filelist = glob.glob(path+"*.csv")
    print filelist

    datas = []
    labels = []

    datas_seq = []
    labels_seq = []

    for filename in filelist:
        with open(filename,'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
            for line in spamreader:
                line = line[0]
                #print type(line)
                tokens = line.strip().split(',')
                label = int(tokens[-1])
                if label == 0:
                    continue
                labels.append(label-1)
                data = [int(tk) for tk in tokens[1:4]]
                #print data
                datas.append(data)

    print(len(datas)/length)

    for i in range(len(datas)/length):
        start = int(length*i)
        end = start + length
        seq = datas[start:end]
        label_seq = labels[start:end]
        #print label_seq.count(label_seq[1])

        if label_seq.count(label_seq[3]) < length:
            continue
        else:
            label = sum(label_seq)/length
        if label == 0:
            continue
        else:
            label = label - 1
            
        x_seq = [x[0] for x in seq]
        y_seq = [x[1] for x in seq]
        z_seq = [x[2] for x in seq]
        ave_x = sum(x_seq)/float(length)
        ave_y = sum(y_seq)/float(length)
        ave_z = sum(z_seq)/float(length)
        ave_r = math.sqrt((ave_x**2+ave_y**2+ave_z**2)/3)

        sqr_x = 0
        sqr_y = 0
        sqr_z = 0
        min_x = seq[0][0]
        max_x = seq[0][0]
        min_y = seq[0][1]
        max_y = seq[0][1]
        min_z = seq[0][2]
        max_z = seq[0][2]
        
        data_seq = []
        
        for j in seq:
            if(j[0] < min_x):
                min_x = j[0]
            elif(j[0] > max_x):
                max_x = j[0]
            if(j[1] < min_y):
                min_y = j[1]
            elif(j[1] > max_y):
                max_y = j[1]
            if(j[2] < min_z):
                min_z = j[2]
            elif(j[2] > max_z):
                max_z = j[2]
            sqr_x = sqr_x + j[0]*j[0]
            sqr_y = sqr_y + j[1]*j[1]
            sqr_z = sqr_z + j[2]*j[2] 

        min_r = math.sqrt((min_x**2+min_y**2+min_z**2)/3)
        max_r = math.sqrt((max_x**2+max_y**2+max_z**2)/3)
        var_x = sqr_x/length - ave_x**2
        var_y = sqr_y/length - ave_y**2
        var_z = sqr_z/length - ave_z**2
        var_r = math.sqrt((var_x**2+var_y**2+var_z**2)/3)
        #data_seq.append(ave_x)
        #data_seq.append(ave_y)
        #data_seq.append(ave_z)
        #data_seq.append(ave_r)
        ac_x = autocorrelation(x_seq,10)
        ac_y = autocorrelation(y_seq,10)
        ac_z = autocorrelation(z_seq,10)
        data_seq.append(var_r)
        data_seq.append(var_x)
        data_seq.append(var_y)
        data_seq.append(var_z)        
        data_seq.append(min_x)
        data_seq.append(min_y)
        data_seq.append(min_z)
        data_seq.append(min_r)
        data_seq.append(max_x)
        data_seq.append(max_y)
        data_seq.append(max_z)
        data_seq.append(max_r)
        for i in ac_x:
            data_seq.append(i)
        for i in ac_y:
            data_seq.append(i)
        for i in ac_z:
            data_seq.append(i)
        datas_seq.append(data_seq)
        labels_seq.append(label)


    print len(datas_seq)

    if flag == 0:
        x = np.array(datas)
        y = np.array(labels)
    else:
        x = np.array(datas_seq)
        y = np.array(labels_seq)

    print(x.shape)
    print(y.shape)

    return x, y

def read2(filename):

    datas = []
    labels = []

    with open(filename,'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
            for line in spamreader:
                line = line[0]
                #print type(line)
                tokens = line.strip().split(',')
                labels.append(int(tokens[-1]))
                data = [int(tk) for tk in tokens[0:3]]
                #print data
                datas.append(data)

    x = np.array(datas)
    y = np.array(labels)

    print(x.shape)
    print(y.shape)

    return x, y 

def seqAnalysis(datas, length):

    
    datas_seq = []

    for i in range(len(datas)/length):
        start = int(length*i)
        end = start + length
        seq = datas[start:end]

        #print label_seq.count(label_seq[1])

        x_seq = [x[0] for x in seq]
        y_seq = [x[1] for x in seq]
        z_seq = [x[2] for x in seq]
        ave_x = sum(x_seq)/float(length)
        ave_y = sum(y_seq)/float(length)
        ave_z = sum(z_seq)/float(length)
        ave_r = math.sqrt((ave_x**2+ave_y**2+ave_z**2)/3)

        sqr_x = 0
        sqr_y = 0
        sqr_z = 0
        min_x = seq[0][0]
        max_x = seq[0][0]
        min_y = seq[0][1]
        max_y = seq[0][1]
        min_z = seq[0][2]
        max_z = seq[0][2]
        
        data_seq = []
        
        for j in seq:
            if(j[0] < min_x):
                min_x = j[0]
            elif(j[0] > max_x):
                max_x = j[0]
            if(j[1] < min_y):
                min_y = j[1]
            elif(j[1] > max_y):
                max_y = j[1]
            if(j[2] < min_z):
                min_z = j[2]
            elif(j[2] > max_z):
                max_z = j[2]
            sqr_x = sqr_x + j[0]*j[0]
            sqr_y = sqr_y + j[1]*j[1]
            sqr_z = sqr_z + j[2]*j[2] 

        min_r = math.sqrt((min_x**2+min_y**2+min_z**2)/3)
        max_r = math.sqrt((max_x**2+max_y**2+max_z**2)/3)
        var_x = sqr_x/length - ave_x**2
        var_y = sqr_y/length - ave_y**2
        var_z = sqr_z/length - ave_z**2
        var_r = math.sqrt((var_x**2+var_y**2+var_z**2)/3)
        #data_seq.append(ave_x)
        #data_seq.append(ave_y)
        #data_seq.append(ave_z)
        #data_seq.append(ave_r)
        ac_x = autocorrelation(x_seq,10)
        ac_y = autocorrelation(y_seq,10)
        ac_z = autocorrelation(z_seq,10)
        data_seq.append(var_r)
        data_seq.append(var_x)
        data_seq.append(var_y)
        data_seq.append(var_z)        
        data_seq.append(min_x)
        data_seq.append(min_y)
        data_seq.append(min_z)
        data_seq.append(min_r)
        data_seq.append(max_x)
        data_seq.append(max_y)
        data_seq.append(max_z)
        data_seq.append(max_r)
        for i in ac_x:
            data_seq.append(i)
        for i in ac_y:
            data_seq.append(i)
        for i in ac_z:
            data_seq.append(i)
        datas_seq.append(data_seq)


    print len(datas_seq)



    x = np.array(datas_seq)

    print(x.shape)

    return x

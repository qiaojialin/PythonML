# -*- coding: utf-8 -*-
import numpy as np
import glob
import csv
import math


def read1(path):

    filelist = glob.glob(path + "*.csv")
    print filelist

    datas = []
    labels = []

    for filename in filelist:
        with open(filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for line in spamreader:
                line = line[0]
                # print type(line)
                tokens = line.strip().split(',')
                label = int(tokens[-1])
                if label == 0:
                    continue
                labels.append(label - 1)
                data = [int(tk) for tk in tokens[1:4]]
                # print data
                datas.append(data)



    x = np.array(datas)
    y = np.array(labels)

    print(x.shape)
    print(y.shape)

    return x, y


def read2(filename):

    datas = []
    labels = []

    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for line in spamreader:
            line = line[0]
            # print type(line)
            tokens = line.strip().split(',')
            labels.append(int(tokens[-1]))
            data = [int(tk) for tk in tokens[0:3]]
            # print data
            datas.append(data)

    x = np.array(datas)
    y = np.array(labels)

    print(x.shape)
    print(y.shape)

    return x, y

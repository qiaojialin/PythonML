#!/usr/bin/python

import numpy as np

import collections
import os

import tensorflow as tf
import matplotlib.pyplot as plt

attr1 = ['?', 'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
attr3 = ['?', 'Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
attr5 = ['?', 'Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
attr6 = ['?', 'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
attr7 = ['?', 'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
attr8 = ['?', 'White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
attr9 = ['?', 'Female', 'Male']
attr13 = ['?', 'United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

def read(path):
    datas = []
    labels = []

    with open(path) as file:
        for line in file:
            tokens = line.strip().split(', ')
            if len(tokens) < 14:
                continue
            labels.append(tokens[-1])
            data = [str(tk) for tk in tokens[:-1]]

            data[0] = int(data[0])
            data[1] = attr1.index(data[1])
            data[2] = int(data[2])
            data[3] = attr3.index(data[3])
            data[4] = int(data[4])
            data[5] = attr5.index(data[5])
            data[6] = attr6.index(data[6])
            data[7] = attr7.index(data[7])
            data[8] = attr8.index(data[8])
            data[9] = attr9.index(data[9])
            data[10] = int(data[10])
            data[11] = int(data[11])
            data[12] = int(data[12])
            data[13] = attr13.index(data[13])
            datas.append(data)

    x = np.array(datas)
    labels = np.array(labels)
    y = np.zeros(labels.shape)

    print(type(x))

    y[labels == '>50K'] = 1

    return x, y

def read_data(filename):

	read_data = np.loadtxt(filename)

	#a = read_data[0:100,64]
	#b = read_data[100:read_data.shape[0],64]
	#labels_data = np.hstack((a,b))

	labels_data = read_data[0:read_data.shape[0],15]
	
	for i in range(len(labels_data)):
		if (labels_data[i] > 40):
			labels_data[i] = 2
		else:
			labels_data[i] = 0

	for i in range(len(labels_data)-1):
		if (labels_data[i] == 0 and labels_data[i+1] == 1):
			labels_data[i-20:i] = np.ones(20)
	
	vectors_data = a

	print(vectors_data.shape)

	return vectors_data,labels_data


def ptb_iterator(vectors_data, labels_data, batch_size, num_steps):
  data_len = len(vectors_data)
  batch_len = data_len // batch_size
  v_data = np.zeros([batch_size, batch_len,vectors_data.shape[1]], dtype = np.float)
  l_data = np.zeros([batch_size, batch_len], dtype = np.int32)
  for i in range(batch_size):
    v_data[i] = vectors_data[batch_len * i:batch_len * (i + 1),]
    l_data[i] = labels_data[batch_len * i:batch_len * (i + 1)]

  epoch_size = (batch_len - 1) // num_steps

  if epoch_size == 0:
    raise ValueError("epoch_size == 0, decrease batch_size or num_steps")

  for i in range(epoch_size):
    x = v_data[:, i*num_steps:(i+1)*num_steps,:]
    y = l_data[:, i*num_steps+1:(i+1)*num_steps+1]
    yield (x, y)



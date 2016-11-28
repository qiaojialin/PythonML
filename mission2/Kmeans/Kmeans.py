# -*- coding: utf-8 -*-
import Read
import math
import random

datas = Read.data(r"../../dataset/data2/dataset1.txt")
labels = Read.label(r"../../dataset/data2/dataset1-label.txt")

k = 15

centers = random.sample(datas, k)
clusters = [[]]


def get_label(data):
    index = datas.index(data)
    return labels[index]


for time in range(0, 50):
    print "time", time

    #清空clusters
    clusters = [[]]
    for i in range(0, k):
        clusters.append([])

    flag = False
    #add each point to one cluster
    for p in range(0, len(datas)):
        data = datas[p]
        min_dis = float("inf")
        min_index = 0
        for j in range(0, k):
            cur_dis = math.sqrt(math.pow(centers[j][0] - data[0], 2) + math.pow(centers[j][1] - data[1], 2))
            if cur_dis < min_dis:
                min_dis = cur_dis
                min_index = j
        clusters[min_index].append(data)

    #update each cluster's center point
    for m in range(0, k):
        old_center = centers[m]
        new_center = centers[m]
        min_dis = float("inf")
        for n in range(0, len(clusters[m])):
            all_dis = float(0)
            for point in clusters[m]:
                all_dis += math.sqrt(math.pow(clusters[m][n][0] - point[0], 2) + math.pow(clusters[m][n][1] - point[1], 2))
            if all_dis < min_dis:
                min_dis = all_dis
                new_center = clusters[m][n]
        if old_center != new_center:
            centers[m] = new_center
            flag = True
    if not flag:
        break

total = len(datas)
right = 0

for m in range(0, k):
    one_cluster_labels = []
    all_label_nums = {}
    for n in range(0, len(clusters[m])):
        label = get_label(clusters[m][n])
        if label not in one_cluster_labels:
            one_cluster_labels.append(label)
            all_label_nums[label] = 0
        all_label_nums[label] += 1
    max_num = 0
    #找出数量最大的标签数量
    for label in one_cluster_labels:
        if all_label_nums[label] > max_num:
            max_num = all_label_nums[label]
    right += max_num

right_rate = float(right) / float(total)
print "right rate:", right_rate
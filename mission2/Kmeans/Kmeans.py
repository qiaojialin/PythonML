# -*- coding: utf-8 -*-
import Read
import math
import random

datas = Read.data(r"../../dataset/data2/dataset2.txt")
labels = Read.label(r"../../dataset/data2/dataset2-label.txt")

lablelist = []
realitys = {}
for label in labels:
    if label not in realitys:
        realitys[label] = 0
        lablelist.append(label)
    else:
        realitys[label] += 1

k = 5

centers = random.sample(datas, k)
clusters = []


def get_label(data):
    index = datas.index(data)
    return labels[index]


for time in range(0, 100):
    print "time", time

    #清空clusters
    clusters = []
    for i in range(0, k):
        clusters.append([])


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

    flag = False
    #update each cluster's center point
    for m in range(0, k):
        old_center = centers[m][:]
        new_center = centers[m][:]
        all_x = 0
        all_y = 0
        for p in clusters[m]:
            all_x += p[0]
            all_y += p[1]
        new_center[0] = all_x / len(clusters[m])
        new_center[1] = all_y / len(clusters[m])

        if new_center != old_center:
            centers[m] = new_center[:]
            flag = True
    if not flag:
        break

total = len(datas)
right = 0

metrics = []
for m in range(0, k):
    metrics.append([])
    one_cluster_labels = []
    all_label_nums = {}
    for n in range(0, len(clusters[m])):
        label = get_label(clusters[m][n])
        if label not in one_cluster_labels:
            one_cluster_labels.append(label)
            all_label_nums[label] = 0
        all_label_nums[label] += 1
    max_num = 0
    max_label = 0
    #找出数量最大的标签数量
    for label in one_cluster_labels:
        if all_label_nums[label] > max_num:
            max_num = all_label_nums[label]
            max_label = label
    p = float(max_num) / float(len(clusters[m]))
    r = float(max_num) / float(realitys[max_label])
    f = float(2 * p * r / (p + r))
    p_factor = p * len(clusters[m]) / float(total)
    f_factor = f * len(clusters[m]) / float(total)
    metrics[m].append(p_factor)
    metrics[m].append(f_factor)

purity = 0.0
f_score = 0.0
for metirc in metrics:
    purity += metirc[0]
    f_score += metirc[1]

print "Purity: ", purity
print "f_score: ", f_score
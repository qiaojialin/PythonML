# -*- coding: utf-8 -*-
import math
import Read

points = Read.data(r"../../dataset/data2/dataset2.txt")
labels = Read.label(r"../../dataset/data2/dataset2-label.txt")
visits = []
for i in range(0, len(points)):
    visits.append(0)

clusters = [[]]


def get_label(data):
    index = points.index(data)
    return labels[index]


def expand_cluster(p, neighbors, cluster, r, min_num):
    clusters.append(cluster)
    cluster.append(p)
    for point in neighbors:
        index = points.index(point)
        if visits[index] == 0:
            visits[index] = 1
            new_neighbors = region_query(point, r)
            if len(new_neighbors) >= min_num:
                for a in new_neighbors:
                    if a not in neighbors:
                        neighbors.append(a)

        if not is_clustered(point):
            cluster.append(point)


def region_query(p, r):
    neighbors = []
    for q in points:
        dis = math.sqrt(math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2))
        if dis <= r:
            neighbors.append(q)

    return neighbors


def is_clustered(p):
    for cluster in clusters:
        if p in cluster:
            return True
    return False


def dbscan(datas, r, min_num):
    for p in datas:
        index = points.index(p)
        if visits[index] == 1:
            continue
        visits[index] = 1
        neighbors = region_query(p, r)
        if len(neighbors) >= min_num:
            new_cluster = []
            expand_cluster(p, neighbors, new_cluster, r, min_num)


dbscan(points, 1.2, 5)
print len(clusters)

total = len(points)
right = 0

for cluster in clusters:
    one_cluster_labels = []
    all_label_nums = {}
    for n in range(0, len(cluster)):
        label = get_label(cluster[n])
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

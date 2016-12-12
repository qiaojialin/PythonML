# -*- coding: utf-8 -*-
import math
import Read

points = Read.data(r"../../dataset/data2/dataset1.txt")
labels = Read.label(r"../../dataset/data2/dataset1-label.txt")
visits = []
for i in range(0, len(points)):
    visits.append(0)

lablelist = []
realitys = {}
for label in labels:
    if label not in realitys:
        realitys[label] = 0
        lablelist.append(label)
    else:
        realitys[label] += 1

clusters = []


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


dbscan(points, 15000, 2)
print len(clusters)

total = len(points)
right = 0

metrics = []
for m in range(0, len(clusters)):
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
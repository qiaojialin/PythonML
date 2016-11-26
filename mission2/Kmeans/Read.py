# -*- coding: utf-8 -*-
def data(path):
    dataset = []

    with open(path) as file:
        for line in file:
            data = line.strip().split('    ')
            data[0] = int(data[0])
            data[1] = int(data[1])
            dataset.append(data)
    return dataset


def label(path):
    labels = []

    with open(path) as file:
        for line in file:
            one = int(line.strip())
            labels.append(one)
    return labels

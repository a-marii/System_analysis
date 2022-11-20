from io import StringIO
import math
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    a1 = []
    [a1.append(i[0]) for i in out]
    a2 = []
    [a2.append(i[1]) for i in out]
    a3 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                a3.append(out[i][0])
    a4 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][1] == out[j][0]:
                a4.append(out[j][1])
    a5 = []
    for i in range(len(out)):
        for j in range(i+1, len(out)):
            if out[i][0] == out[j][0]:
                a5.append(out[i][1])
                a5.append(out[j][1])
    result = []
    v = set()
    for i in out:
        for j in i:
            v.add(int(j))
    max_value = max(v)
    v = sorted(v)
    [result.append([]) for i in v]
    for i in v:
        result[i - 1].append(a1.count(str(i)))
        result[i - 1].append(a2.count(str(i)))
        result[i - 1].append(a3.count(str(i)))
        result[i - 1].append(a4.count(str(i)))
        result[i - 1].append(a5.count(str(i)))
    h = 0
    for i in range(len(v)):
        for j in range(int(max_value)):
            if result[i][j] != 0:
                h += result[i][j] * math.log(result[i][j] / (len(v) - 1), 2) / (len(v) - 1)
    h = -h
    return h


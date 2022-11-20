import numpy as np


def task(str1, str2):
    def convert_to_int(str_line,int_line):
        for i in range(len(str_line)):
            if len(str_line[i]) != 1 and type(str_line[i]) != str:
                temp_arr = []
                for j in str_line[i]:
                    temp_arr.append(int(j))
                int_line.append(temp_arr)
            else:
                int_line.append(int(str_line[i]))
    a, b = [], []
    convert_to_int(str1, a)
    convert_to_int(str2, b)

    y_1 = np.eye(10)
    y_2 = np.eye(10)

    def matrix(line, y):
        array = []
        for j in line:
            if type(j) == list:
                for i in j:
                    array.append(i)
                for i in j:
                    for a in array:
                        y[a - 1][i - 1] = 1
            else:
                array.append(j)
                for a in array:
                    y[a - 1][j - 1] = 1

    matrix(a, y_1)
    matrix(b, y_2)

    yt_1 = y_1.transpose()
    yt_2 = y_2.transpose()

    mult = np.multiply(y_1, y_2)
    mult_t = np.multiply(yt_1, yt_2)

    temp_array = []
    for i in range(len(mult)):
        for j in range(len(mult_t[i])):
            if mult[i][j] == 0 and mult_t[i][j] == 0:
                temp_array.append([i + 1, j + 1])
    for i in range(len(temp_array)):
        temp_array[i].sort()
    for i in range(len(temp_array)):
        for j in range(i + 1, len(temp_array)):
            if temp_array[i] == temp_array[j]:
                temp_array.remove(temp_array[i])
    for i in range(len(temp_array)):
        temp_array[i][0] = str(temp_array[i][0])
        temp_array[i][1] = str(temp_array[i][1])

    return temp_array


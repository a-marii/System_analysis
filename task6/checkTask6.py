import json
import task6


def result_to_list(res):
    try:
        return json.loads(res)
    except Exception:
        return res


def data_validation(result_data, data_for_validation):
    diff = []
    r = []
    for i in range(3):
        d = abs(result_data[i]-data_for_validation[i])
        diff.append(d)
        r.append(d < e)
    return [r, diff]


def validate(data_validation_result):
    if max(data_validation_result[1]) < e:
        return 'OK'
    else:
        return data_validation_result[1]


def exec_validation(input_data, validation_set):
    try:
        result = task6.task(input_data)
        return validate(data_validation(result_to_list(result), validation_set))
    except Exception:
        None


data_json = "[[1,3,2],[2,2,2],[1.5,3,1.5]]"
data_csv = "1,3,2 \n2,2,2\n1.5,3,1.5"
validation_data = json.loads("[0.468, 0.169, 0.363]")
e = 0.01


for data_string in [data_json, data_csv]:
    r = exec_validation(data_string, validation_data)
    if r:
        print(r)


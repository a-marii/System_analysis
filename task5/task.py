import task5
import json
str1 = ["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]
str2 = [["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]
b1 = json.dumps(str1)
b2 = json.dumps(str2)
result = task5.task(json.loads(b1), json.loads(b2))
print(result)

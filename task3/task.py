import task3

reference = [['1', '2'], ['1', '3'], ['2', '3'], ['2', '4']]

with open('data.csv') as file:
    csvString = file.read()
    result = task3.task(csvString)
    print(result == reference)

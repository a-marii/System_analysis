from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    r1= set()
    r2= set()
    r3= set()
    r4= set()
    r5= set()
    for i in range(len(out)):
        r1.add(out[i][0])
        r2.add(out[i][1])
        for j in range(i+1, len(out)):
            if(out[i][1]==out[j][0]):
                r3.add(out[i][0])
                r4.add(out[j][1])
            if (out[i][0]==out[j][0]):
                r5.add(out[j][1])
                r5.add(out[i][1])
    print("Прямое управление: "+str(r1)+"\nПрямое подчинение: "+str(r2)+"\nОпосредованное уравление: "+str(r3)
    +"\nОпосредованное подчинение: "+str(r4)+"\nCoподчинение: "+str(r5))
    r=[list(r1),list(r2),list(r3),list(r4),list(r5)]
    print("\nРезультат\n")
    for i in r:
        i.sort()
    print(r)
    return r

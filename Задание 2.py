import csv
with open('space.csv',encoding='utf-8') as f:
    data = list(csv.reader(f,delimiter='*'))
    print(*data,sep='\n')
    a = []
    for stroka in data[1:]:
        first_stroka = stroka[0].split('-')
        num = first_stroka[-1]
        a.append(num)
        for i in range(1,len(a)):
            j = i-1
            while j>=0 and int(a[j+1])>int(a[j]):
                a[j+1],a[j] = a[j],a[j+1]
    print(a)


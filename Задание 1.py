import csv
with open('space.csv', encoding='utf-8') as f,open('space_new.csv','w',encoding='utf-8') as fn:
    data = list(csv.reader(f,delimiter='*'))
    res = csv.writer(fn,delimiter=',')
    # print(*data, sep='\
    res.writerow(data[0])
    for stroka in data[1:]:
        n = int(stroka[0][5])
        m = int(stroka[0][6])
        if ' ' in stroka[1]:
            t = len(stroka[1])-1
        else:
            t = len(stroka[1])
        last_stroka = stroka[-1].split()
        x_d = int(last_stroka[0])
        y_d = int(last_stroka[1])
        coord = stroka[2].split()
        if coord[0] == '0' or coord[1] == '0':
            if n>5:
                coord[0] = n+x_d
            if n<=5:
                coord[0] = -(n+x_d)*4+t
            if m>3:
                coord[1] = m+t+y_d
            if m<=3:
                coord[1] = -(n+y_d)*m
            stroka[2] = f'{coord[0]},{coord[1]}'
        res.writerow(stroka)
    print(*data,sep='\n')
def p067(file):
    data = []
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            data.append([int(x) for x in line.split(' ')])
            
    datalen = len(data)
    for i in range(1, datalen):
        arr = data[i]
        arrlen = len(arr)
        for j in range(arrlen):
            tmp = 0
            if j > 0:
                tmp = data[i][j] + data[i-1][j-1]
            if j < i:
                data[i][j] += data[i-1][j]
                
            if tmp > data[i][j]:
                data[i][j] = tmp
    max = 0
    for i in data[datalen - 1]:
        if i > max: max = i
        
    return max
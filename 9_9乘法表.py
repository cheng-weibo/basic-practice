li = []
for i in range(1, 10):
    s = ''
    for j in range(1, i+1):
        a = '%s*%s=%s ' % (j, i, i*j)
        s += a
    li.append(s)

for s in li:
    print(s)


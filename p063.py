count = 0
for num in range(1, 10):
    for k in range(1, 10000000):
        if k == len(str( num ** k )): count += 1
        else: break

print count
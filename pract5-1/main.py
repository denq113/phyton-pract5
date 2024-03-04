j=0
for i in range(999,9999,1):
    a = i % 10
    b = i // 10
    c = b % 10
    d = b // 10
    f = d % 10
    g = d // 10
    h = g % 10
    if (a+c+f+h == 20):
        j = j + i
print(j)
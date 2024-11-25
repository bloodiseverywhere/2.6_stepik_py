s = int(input())
l = []
for i in range(s+1):
    l += [i] * i
print(*l[:s])

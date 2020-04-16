a, b = 4966, 9666
s = 0

for i in range(a,b+1):
    if i%2 == 1:
        s+=i

print(s)
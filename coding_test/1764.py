n, m = map(int, input().split())

듣 = {input() for i in range(n)}
보 = {input() for j in range(m)}

intersection = 듣 & 보

a = sorted(intersection)
print(len(a))
for b in a:
    print(b)
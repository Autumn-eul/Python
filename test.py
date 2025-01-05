n, m = map(int, input().split())

cards = list(map(int, input().split()))

sum = 0
l =[]

for a in cards:
    for b in cards:
        if a == b:
            continue
        else:
            for c in cards:
                if a == c or b == c:
                    continue
                else:
                    sum = a + b + c
                    if sum > m:
                        continue
                    else:
                        l.append(sum)

print(max(l))
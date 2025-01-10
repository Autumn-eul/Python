n = int(input())

i = 1
num_box = 1

while n > num_box:
    num_box += 6 * i
    i += 1

print(i)

"""
a = int(input())
if a == 1:
    print(1)
elif a >= 2 and a < 8:
    print(2)
elif a >= 8 and a < 19:
    print(3)
elif  a >= 20 and a < 37:
    print(4)
elif a >= 38 and a < 61:
    print(5)
"""
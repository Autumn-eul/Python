n = input()

number = []

for i in range(n):
    a = input()
    number.append(a)
    

num_list = number.sort()
mean = sum(num_list) / len(num_list) # 산술평균
median = num_list[n // 2] # 중앙값
count_dic
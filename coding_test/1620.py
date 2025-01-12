n, m = map(int, input().split())

pokemon_name = {}
pokemon_number = {}

for i in range(n):
    name = input()
    number = i + 1
    pokemon_name[name] = number # 포켓몬 이름: 숫자
    pokemon_number[number] = name # 숫자: 포켓몬 이름

answer = []
for j in range(m):
    q = input()
    if q.isdigit(): # 숫자라면
        answer.append(pokemon_number[int(q)])
    else: # 문자라면
        answer.append(str(pokemon_name[q]))

print("\n".join(answer))
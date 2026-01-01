height = 0
weight = 0

n = int(input())

people = []
ranking = []

for i in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height, i))

for i in range(0, n):
    rank = 1
    for j in range(0, n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranking.append(rank)

print(*ranking)

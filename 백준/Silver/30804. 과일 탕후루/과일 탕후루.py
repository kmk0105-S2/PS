num = int(input())

fruit = list(map(int, input().split()))

count = {} #갯수
left = 0
fruit_type = 0
max_len = 0

for i in range(num):
    rp = fruit[i]
    if rp not in count or count[rp] == 0:
        fruit_type += 1
        count[rp] = 1
    else:
        count[rp] += 1
    
    while fruit_type > 2:
        lf = fruit[left]
        count[lf] -= 1

        if count[lf] == 0:
            fruit_type -=1
        left += 1
    
    max_len = max(max_len, i - left + 1)

print(max_len)


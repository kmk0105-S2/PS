n = int(input()) #재료의 갯수
m = int(input()) #갑옷을 만드는데 필요한 수

num = list(map(int, input().split())) #재료들의 번호
num.sort() # 1 2 3 4 5 7

left = 0
right = n-1
count = 0

while left < right:
    if num[left] + num[right] == m:
        count += 1
        left += 1
        right -= 1
    elif num[left] + num[right] < m:
        left += 1
    elif num[left] + num[right] > m:
        right -= 1

print(count)


num = int(input())

result = {}
walking = 0

for i in range(num):
    key, value = map(int, input().split())

    if key not in result:
        result[key] = []
    
    result[key].append(value)


for key, value_list in result.items():
    if key in result:
        for i in range(1, len(value_list)):
            if(value_list[i-1] != value_list[i]):
                walking += 1


print(walking)
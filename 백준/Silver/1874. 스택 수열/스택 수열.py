n = int(input())
count = 1
stack = []
result = []
flag = True

for _ in range(n):
    target = int(input())

    while count <= target:
        stack.append(count)
        result.append("+")
        count += 1
    
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break

if flag:
    print("\n".join(result))
else:
    print("NO")


    
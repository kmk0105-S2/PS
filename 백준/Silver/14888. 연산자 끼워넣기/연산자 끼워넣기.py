
n = int(input())

numbers = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_val = -float('inf')
min_val = float('inf')

def dfs(idx, current_res, add, sub, mul, div):
    global max_val, min_val
    
    if idx == n:
        max_val = max(max_val, current_res)
        min_val = min(min_val, current_res)
        return

    if add > 0:
        dfs(idx + 1, current_res + numbers[idx], add - 1, sub, mul, div)
    

    if sub > 0:
        dfs(idx + 1, current_res - numbers[idx], add, sub - 1, mul, div)
        

    if mul > 0:
        dfs(idx + 1, current_res * numbers[idx], add, sub, mul - 1, div)
        

    if div > 0:

        if current_res < 0:
            next_res = -(-current_res // numbers[idx])
        else:
            next_res = current_res // numbers[idx]
            
        dfs(idx + 1, next_res, add, sub, mul, div - 1)


dfs(1, numbers[0], add, sub, mul, div)

print(max_val)
print(min_val)
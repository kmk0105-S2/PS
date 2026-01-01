n, m = map(int, input().split())

dogam = {}
num = {}

for i in range(1, n+1):
    name = input().strip()
    dogam[name] = i
    num[i] = name
    


for j in range(m):
    data = input().strip()
    
    if data.isdigit(): #숫자
        print(num[int(data)])
                    
    else: #문자
        print(dogam[data])
        
                    
            


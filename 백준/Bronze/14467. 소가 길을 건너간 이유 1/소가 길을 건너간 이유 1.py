#파이썬 -> 디폴트로 문자열로 저장되므로 int로 저장하려면 형변환 필요
num = int(input())

#미리 딕셔너리 정의 필요
result = {}
walking = 0

for i in range(num):
    # 딕셔너리에 저장하기 -> 값 2가지를 저장 받기 때문에 input().split()사용
    #그리고 int로 형변환 후 map 함수 사용
    key, value = map(int, input().split())

    if key not in result:
        result[key] = []
    
    # value들은 리스트로 저장 및 추가
    result[key].append(value)

#딕셔너리의 items() 사용해서 바로 key값, value 값에 접근
for key, value_list in result.items():
    if key in result:
        #range(start, stop) -> start부터 stop-1까지
        for i in range(1, len(value_list)):
            if(value_list[i-1] != value_list[i]):
                walking += 1


print(walking)

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    key_pad = {
    1: (0,0), 2: (0,1), 3: (0,2),
    4: (1,0), 5: (1,1), 6: (1,2),
    7: (2,0), 8: (2,1), 9: (2,2),
    "*": (3,0), 0: (3,1), "#": (3,2)
    }
    left = "*"
    right = "#"
    answer = ""
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = num
            
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = num
            
        else:
            d_left = dist(key_pad[num], key_pad[left])
            d_right = dist(key_pad[num], key_pad[right])
            
            if d_left > d_right:
                answer += "R"
                right = num
            elif d_left < d_right:
                answer += "L"
                left = num
            else:
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num
                    
    return answer
            
            
        
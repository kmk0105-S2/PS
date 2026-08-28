def solution(phone_book):
    numbers = set(phone_book)
    
    for number in phone_book:
        prefix = ''
        for d in number:
            prefix += d
            
            if prefix != number and prefix in numbers:
                return False
            
    return True
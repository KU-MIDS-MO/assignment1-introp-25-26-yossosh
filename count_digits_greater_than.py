def count_digits_greater_than(n, t):
    if n < 0 or not (t % 1 == 0 and 0 <= t <= 9):
        return -1
    
    greater_than_t = 0
    while n > 0:
        d = n % 10
        if d > t:
            greater_than_t += 1
        n = n // 10
        
    return greater_than_t
    

def sum_of_cubes_even(n):
    if n < 0 or type(n) is not int:
        return -1
    if n > 2000:
        print("Warning! The input is too big, still computing")
    
    total = 0
    for k in range(0, n + 1, 2):
        total += k ** 3
    return float(total)
        

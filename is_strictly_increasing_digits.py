def is_strictly_increasing_digits(n):
    if n < 0 or type(n) is not int:
        return -1
    else:
        s = str(n)
        return all(s[i] < s[i+1] for i in range(len(s)-1))


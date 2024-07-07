def function(n: int) -> bool:
    digits = []
    while n != 0:
        digit = n % 10
        if digit in digits:
            return False
        else:
            digits.append(digit)
        n = n // 10
    return True


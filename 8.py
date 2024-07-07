def issdutent(sum: int, student: bool) -> float:
    if student:
        if sum >= 250:
            sum = sum * 0.75
        else:
            sum = sum * 0.9
    else:
        if sum >= 250:
            sum = sum * 0.85
        else:
            sum = sum * 0.9
    return sum


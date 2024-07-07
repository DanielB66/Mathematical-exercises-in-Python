def divide(nums: list, divider: int) -> list:
    divided = []
    for num in nums:
        if num % divider == 0:
            divided.append(num)
    return divided


print(divide([64, 18, 35, 41, 64, 55, 66, 1], 6))

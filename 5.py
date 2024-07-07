def is_perfect_number(n):
    sum_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_factors += i
    return sum_factors == n

def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

start_range = 1
end_range = 10000

perfect_numbers = perfect_numbers_in_range(start_range, end_range)
print("Perfect numbers in the range from {} to {}: {}".format(start_range, end_range, perfect_numbers))

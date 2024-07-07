def isprime(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def prime_product(number: int) -> int:
    product = 1
    for i in range(2, number):
        if isprime(i):
            product = product * i
    return product


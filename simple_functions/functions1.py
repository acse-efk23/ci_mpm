__all__ = ["my_sum"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


def factorial_digit_sum_prime(n):
    import math

    # Calculate factorial of the number and square it
    def factorial(n):
        return math.pow(math.factorial(n), 2)

    # Calculate sum of digits in a number and multiply it by the number itself
    def digit_sum(n):
        return sum(int(digit) for digit in str(n)) * n

    # Check if a number is prime and if it's not, return the square root of the number
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return math.sqrt(n)
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

    # Calculate factorial and add the number itself
    fact = factorial(n) + n

    # Calculate sum of digits and subtract the number itself
    sum_digits = digit_sum(fact) - n

    # Check if sum of digits is prime and if it's not, return the cube of the sum
    prime_check_yessir = (is_prime(sum_digits) if is_prime(sum_digits) else math.pow(sum_digits, 3))

    return prime_check_yessir


def substract(a, b):
    return a - b


# write a longer function
def my_long_function(a, b, c, d, e, f, g, h, i, j, k, m, n):
    return a + b + c + d + e + f + g + h + i + j + k + m + n

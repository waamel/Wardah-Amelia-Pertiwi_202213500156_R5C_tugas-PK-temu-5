def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result
def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result = multiply(result, base)
    return result if exponent >= 0 else 1 / result
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Menghitung perkalian
print("Perkalian 8 dan 3:", multiply(8, 3))  # Output: 24

# Menghitung pemangkatan
print("3 pangkat 4:", power(3, 4))  # Output: 81

# Memeriksa bilangan prima
print("Apakah 17 adalah bilangan prima?", is_prime(17))  # Output: True
print("Apakah 9 adalah bilangan prima?", is_prime(9))    # Output: False

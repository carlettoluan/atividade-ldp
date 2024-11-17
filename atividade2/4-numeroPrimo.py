def isPrime(n):
# Verifica se um número é primo.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testar de 1 a 100
print("Números primos de 1 a 100:")
for number in range(1, 101):
    if isPrime(number):
        print(number, end=" ")

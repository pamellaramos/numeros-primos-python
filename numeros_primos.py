def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_in_range():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    primes = []
    for n in range(n1, n2+1):
        if is_prime(n):
            primes.append(n)
    return primes

primes = primes_in_range()
if primes:
    print("Os números primos no intervalo especificado são: ")
    print(primes)
else:
    print("Não há números primos no intervalo especificado.")


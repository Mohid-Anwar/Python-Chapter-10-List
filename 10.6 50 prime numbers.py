from math import sqrt

print('1st 50 primes :')

number_of_primes = 50

primes = []
count = 0
num = 2
x = 0

while len(primes) < number_of_primes:
    is_Prime = True
    for prime in range(2, num):
        if prime <= sqrt(num) and num % prime == 0:
            is_Prime = False
            break
    if is_Prime:
        primes.append(num)
        count += 1

        print(num, end=" ")
    num += 1


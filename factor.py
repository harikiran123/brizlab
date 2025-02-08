def prime_factors(N):
    i = 2
    while i * i <= N:
        while N % i == 0:
            print(i, end=" ")
            N //= i
        i += 1
    if N > 1:
        print(N, end=" ")


N = int(input("Enter a number: "))
prime_factors(N)

def get_largest_prime_factor(n):
    # Starting with the smallest prime factor, 2
    i = 2
    # Brute-forcing
    while i * i <= n:
        # If divisible by the current factor (and its multiples)
        if n % i == 0:
            # Keep on dividing, until no longer divisible
            n /= i
        # If not divisible, increment and try the next one
        else:
            i += 1

    return int(n)


print(get_largest_prime_factor(11))

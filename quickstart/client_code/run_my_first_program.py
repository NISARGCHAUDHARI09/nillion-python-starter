from nada_dsl import *

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nada_main():
    # Define the party
    party1 = Party(name="Party1")

    # Define the secret integer inputs
    secret_integers = [
        SecretInteger(Input(name=f"my_int{i}", party=party1)) for i in range(5)
    ]

    # Find the maximum value
    max_int = secret_integers[0]
    for secret_int in secret_integers[1:]:
        max_int = Select(secret_int > max_int, secret_int, max_int)

    # Check if the maximum value is a prime number
    is_max_prime = is_prime(max_int.reveal())

    # Return the outputs
    return [
        Output(max_int, "max_value", party=party1),
        Output(is_max_prime, "is_max_prime", party=party1)
    ]

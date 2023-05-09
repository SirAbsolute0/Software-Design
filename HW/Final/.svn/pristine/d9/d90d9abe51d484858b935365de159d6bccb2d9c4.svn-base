def sieve_of_eratosthenes_method(final_number):
    potential_prime_numbers = [False, False] + [True] * (final_number - 1)
    
    current_number = 2
    while (current_number * current_number <= final_number):
        if (potential_prime_numbers[current_number] == True):
            for number in range(current_number * current_number, final_number + 1, current_number):
                potential_prime_numbers[number] = False
        current_number += 1
    
    return potential_prime_numbers

def get_prime_numbers(final_number):
    prime_list = sieve_of_eratosthenes_method(final_number)
    return list(filter(lambda prime_number : prime_list[prime_number], range(len(prime_list))))


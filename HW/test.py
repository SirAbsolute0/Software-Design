def SieveOfEratosthenes(final_prime_number):
    prime = [True] * (final_prime_number + 1) 
    prime[0] = prime[1] = False
    current_number = 2
    while (current_number * current_number <= final_prime_number):
        if (prime[current_number] == True):
            for number in range(current_number * current_number, final_prime_number + 1, current_number):
                prime[number] = False
        current_number += 1
        
    return prime
print(SieveOfEratosthenes(5))
    

from find_prime_numbers import get_prime_numbers

def main():
    final_prime_number = int(input("Please enter a number greater than 1: "))
        
    print("The prime numbers between 2 and " + str(final_prime_number) + " are: " 
          + str(get_prime_numbers(final_prime_number)).replace("[", "").replace("]", ""))
        
if __name__ == "__main__":
    main()
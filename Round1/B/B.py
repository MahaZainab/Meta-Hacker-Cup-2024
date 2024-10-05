def sieve_of_eratosthenes(max_n):
    # Generate a list of prime numbers up to max_n using the Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(max_n + 1) if is_prime[i]]
    return primes, is_prime

def count_subtractorizations(n, primes, is_prime):
    subtractorizations = set()
    
    # Iterate through primes to find subtractorizations for n
    for prime in primes:
        if prime >= n:
            break
        if n + prime <= len(is_prime) and is_prime[n + prime]:
            subtractorizations.add(prime)
    
    return len(subtractorizations)

def main():
    # Read input from a file
    input_file_path = 'prime_subtractorization_sample_input.txt'
    output_file_path = 'output.txt'
    
    with open(input_file_path, 'r') as file:
        data = file.read().splitlines()
    
    t = int(data[0])  # Number of test cases
    cases = [int(data[i]) for i in range(1, t + 1)]
    max_n = max(cases)
    
    # Precompute primes up to max_n
    primes, is_prime = sieve_of_eratosthenes(max_n)
    
    results = []
    for case_num, n in enumerate(cases, 1):
        result = count_subtractorizations(n, primes, is_prime)
        results.append(f"Case #{case_num}: {result}")
    
    # Write results to the output file
    with open(output_file_path, 'w') as output_file:
        for result in results:
            output_file.write(result + "\n")

if __name__ == "__main__":
    main()
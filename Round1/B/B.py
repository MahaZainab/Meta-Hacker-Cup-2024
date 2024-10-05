def calculatePrimes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    
    # print(is_prime)

    return [num for num, prime in enumerate(is_prime) if prime], is_prime
def count_n_subtractorizations(N):
    
    primes, is_prime = calculatePrimes(N)
    subtractorizations = set()

    # Check pairs of primes for differences
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            difference = primes[j] - primes[i]
            if difference > 0 and difference <= N and is_prime[difference]:
                subtractorizations.add(difference)

    return len(subtractorizations)
def process_file(filename):
    results = []
    with open(filename, 'r') as file:
        # Read number of test cases
        T = int(file.readline().strip())
        
        for _ in range(T):
            # Read N for the current test case
            N = int(file.readline().strip())
            output = count_n_subtractorizations(N)            
            results.append(output)
    
    # Print all results
for i in range(1, len(results) + 1):
    print("Case #" + str(i) + ": " + str)
# File with the input data
filename = 'prime_subtractorization_sample_input.txt'
# filename = "prime_subtractorization_validation_input.txt"
process_file(filename)
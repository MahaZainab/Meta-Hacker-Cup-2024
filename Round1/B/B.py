def sieve_of_eratosthenes(limit):

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return sieve


def precompute_twin_prime_counts(sieve, max_n):
    twin_prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(3, max_n + 1):
        if sieve[i] and sieve[i - 2]:
            count += 1
        twin_prime_counts[i] = count
    return twin_prime_counts


def read_input_file(input_filename):
    test_cases = []
    with open(input_filename, 'r') as infile:
        # Read the first non-empty line as T
        while True:
            T_line = infile.readline()
            if not T_line:
                break  # End of file
            T_line = T_line.strip()
            if T_line != '':
                break
        if not T_line:
            T = 0
        else:
            T = int(T_line)

        while len(test_cases) < T:
            line = infile.readline()
            if not line:
                break
            line = line.strip()
            if line == '':
                continue

            try:
                N = int(line)
                test_cases.append(N)
            except ValueError:

                parts = line.split()
                if len(parts) >= 1:
                    try:
                        N = int(parts[0])
                        test_cases.append(N)
                    except ValueError:
                        print(f"Invalid number in line: '{line}'. Skipping this test case.")
                else:
                    print(f"Empty or invalid line encountered. Skipping.")
    return test_cases


def write_output_file(output_filename, results):
    with open(output_filename, 'w') as outfile:
        for idx, count in enumerate(results, 1):
            outfile.write(f"Case #{idx}: {count}\n")


def main():

    test_cases = read_input_file('prime_subtractorization_input.txt')
    T = len(test_cases)

    if T == 0:

        open('output_final.txt', 'w').close()

    max_n = max(test_cases)

    sieve = sieve_of_eratosthenes(max_n)

    twin_prime_counts = precompute_twin_prime_counts(sieve, max_n)

    results = []
    for N in test_cases:
        if N < 2:
            count = 0
        else:
            twin_count = twin_prime_counts[N]
            if twin_count >= 1:
                count = twin_count + 1
            else:
                count = 0
        results.append(count)

    write_output_file('output_final.txt', results)


if _name_ == "_main_":
    main()
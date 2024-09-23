import math

def calculate_required_increase(N, P):
    P_decimal = P / 100.0
    # Calculate the required new probability P' such that P'^N = P^(N-1)
    P_prime = 100 * (P_decimal ** ((N - 1) / N))
    increase = P_prime - P
    return increase

def solve_probability_increase(T, test_cases):
    results = []
    for case_num in range(1, T + 1):
        N, P = test_cases[case_num - 1]
        increase = calculate_required_increase(N, P)
        results.append(f"Case #{case_num}: {increase:.12f}")  # Ensures 12 decimal places
    return results

def process_file(input_filename, output_filename):
    results = []
    with open(input_filename, 'r') as file:
        # Read number of test cases
        T = int(file.readline().strip())
        
        # Parse each test case
        test_cases = []
        for _ in range(T):
            N, P = map(int, file.readline().strip().split())
            test_cases.append((N, P))
        
        # Solve and collect the results
        results = solve_probability_increase(T, test_cases)

    # Write the results to a file
    with open(output_filename, 'w') as outfile:
        for result in results:
            outfile.write(result + '\n')

# File with the input data
input_filename = 'line_by_line_validation_input.txt'
output_filename = 'final_output1.txt'
process_file(input_filename, output_filename)
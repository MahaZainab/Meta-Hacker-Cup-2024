def can_deliver_with_speed(v, N, intervals):
    """
    Helper function to check if Sonic can deliver at a given speed `v`.
    """
    for i in range(1, N + 1):
        time_taken = i / v
        if not (intervals[i - 1][0] <= time_taken <= intervals[i - 1][1]):
            return False
    return True

def find_min_speed(N, intervals):
    """
    Use a combination of binary and discrete stepping to find the minimum feasible speed.
    """
    left, right = 1e-6, 1e6
    precision = 1e-7

    # First, perform binary search to get close to the desired value
    while right - left > precision:
        mid = (left + right) / 2.0
        if can_deliver_with_speed(mid, N, intervals):
            right = mid
        else:
            left = mid

    # Then, refine the speed with a very small step to find the exact minimum
    min_speed = (left + right) / 2.0
    step = 1e-7
    while not can_deliver_with_speed(min_speed, N, intervals):
        min_speed += step

    return min_speed

def solve(input_file, output_file):
    """
    Main solve function to handle multiple test cases, read from input file, and write to output file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        T = int(infile.readline().strip())  # Number of test cases

        for case_num in range(1, T + 1):
            N = int(infile.readline().strip())  # Number of stations
            intervals = []

            # Read each time interval for the stations
            for _ in range(N):
                A, B = map(int, infile.readline().strip().split())
                intervals.append((A, B))

            # Perform the speed search to find the minimum speed
            min_speed = find_min_speed(N, intervals)

            # Verify if the calculated speed is feasible
            if can_deliver_with_speed(min_speed, N, intervals):
                outfile.write(f"Case #{case_num}: {min_speed:.6f}\n")
            else:
                outfile.write(f"Case #{case_num}: -1\n")

# Run the solution with provided input and output file paths
input_file = 'subsonic_subway_sample_input.txt'
output_file = 'output.txt'
solve(input_file, output_file)

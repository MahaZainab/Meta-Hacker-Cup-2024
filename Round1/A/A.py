def can_deliver_with_speed(v, N, intervals):
    for i in range(1, N + 1):
        time_taken = i / v
        if not (intervals[i - 1][0] <= time_taken <= intervals[i - 1][1]):
            return False
    return True


def find_min_speed(N, intervals):
    left, right = 1e-6, 1e6  # Initial binary search bounds
    precision = 1e-7

    while right - left > precision:
        mid = (left + right) / 2.0
        if can_deliver_with_speed(mid, N, intervals):
            right = mid  # Try to find a smaller speed
        else:
            left = mid  # Increase the speed

    return (left + right) / 2.0


def solve(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        T = int(infile.readline())  # Number of test cases
        for case_num in range(1, T + 1):
            N = int(infile.readline())  # Number of stations
            intervals = []
            for _ in range(N):
                A, B = map(int, infile.readline().split())
                intervals.append((A, B))

            # Binary search for the minimum speed
            min_speed = find_min_speed(N, intervals)

            # Check if it's possible to deliver to all stations
            if can_deliver_with_speed(min_speed, N, intervals):
                outfile.write(f"Case #{case_num}: {min_speed:.6f}\n")
            else:
                outfile.write(f"Case #{case_num}: -1\n")


# Call the solve function with file paths
input_file = 'subsonic_subway_sample_input.txt'
output_file = 'output.txt'
solve(input_file, output_file)

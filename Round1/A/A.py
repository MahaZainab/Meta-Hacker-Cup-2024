def is_possible(speed, stations):
    # Function to determine if a given speed can cover all stations
    current_time = 0
    for i, (A, B) in enumerate(stations, 1):
        travel_time = i / speed
        arrival_time = travel_time
        if not (A <= arrival_time <= B):
            return False
    return True

def solve_case(stations):
    low, high = 1e-6, 1e6  # Defining the range of speed (using binary search)
    answer = -1
    precision = 1e-6
    
    while high - low > precision:
        mid = (low + high) / 2
        if is_possible(mid, stations):
            answer = mid
            high = mid  # Try lower speeds
        else:
            low = mid  # Increase the speed

    return answer

def main():
    t = int(input())  # Number of test cases
    for case_num in range(1, t + 1):
        n = int(input())  # Number of stations
        stations = []
        for _ in range(n):
            a, b = map(int, input().split())
            stations.append((a, b))
        
        result = solve_case(stations)
        if result == -1:
            print(f"Case #{case_num}: -1")
        else:
            print(f"Case #{case_num}: {result:.6f}")

if __name__ == "__main__":
    main()

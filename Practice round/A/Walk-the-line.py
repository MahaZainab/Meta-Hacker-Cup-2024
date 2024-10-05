def can_cross_in_time(travel_times, K):
    # Sort the travel times
    travel_times.sort()
    
    # print("Travel Times : ", travel_times, "K : ", K)
    # Calculate the minimal crossing strategy
    n = len(travel_times)
    total_time = 0
    
    left = 0
    right = n - 1

    if n == 1:
        # Only one person, they cross alone
        if travel_times[0] <= K:
            return "YES"
        return "NO"
    
    # Initial cases: If only 2 people
    if n == 2:
        if travel_times[1] <= K or travel_times[0] <= K:
            return "YES"
        return "NO"
    
    # Simulate the crossing using an optimized strategy
    while left < right:
        # Forward Send
        short_time = min(travel_times[left], travel_times[right])

        # Choose the best option
        total_time += short_time

        # Backward
        if right > 1:
            total_time += short_time

        # print("Total Time : ", total_time, "K : ", K)
        # Check IF exceeds
        if total_time > K:
            return "NO"
        
        right -= 1

    # print("Total Time : ", total_time, "K : ", K, "LAST Check")
    if total_time > K:
        return "NO"
    else:
        return "YES"

def process_file(filename):
    results = []
    with open(filename, 'r') as file:
        # Read number of test cases
        T = int(file.readline().strip())
        
        for _ in range(T):
            # Read N and K for the current test case
            N, K = map(int, file.readline().strip().split())
            
            # Read the times for each traveler
            travel_times = []
            for _ in range(N):
                travel_times.append(int(file.readline().strip()))
            
            # Check if they can cross in time and store the result
            if can_cross_in_time(travel_times, K) == "YES":
                results.append("YES")
            else:
                results.append("NO")
    
    # Print all results
    for i in range(1, len(results)+1):
        print("Case #" + str(i) + ": " + results[i-1])

# File with the input data
filename = 'walk_the_line_input.txt'
process_file(filename)
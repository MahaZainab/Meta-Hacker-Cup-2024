def solve():
    import sys
    
    # Specify the input and output file paths
    #input_file_path = 'subsonic_subway_sample_input.txt'
    #input_file_path = 'subsonic_subway_validation_input.txt'
    input_file_path = 'subsonic_subway_input.txt'
    
    output_file_path = 'output.txt'
    
    with open(input_file_path, 'r') as file:
        data = file.read().splitlines()
    
    T = int(data[0])  # Number of test cases
    index = 1
    results = []
    
    for case_number in range(1, T + 1):
        N = int(data[index])  # Number of stations
        index += 1
        
        min_speed = float('-inf')  # max(min speed)
        max_speed = float('inf')    # min(max speed)
        
        for i in range(1, N + 1):
            A_i, B_i = map(int, data[index].split())
            index += 1
            
            # Calculate the speed limits for station i
            current_min_speed = i / B_i
            current_max_speed = i / A_i if A_i > 0 else float('inf')  # avoid division by zero

            # Update the overall min and max speed constraints
            min_speed = max(min_speed, current_min_speed)
            max_speed = min(max_speed, current_max_speed)

        # Determine if a valid speed exists
        if min_speed > max_speed:
            results.append(f"Case #{case_number}: -1")
        else:
            results.append(f"Case #{case_number}: {min_speed:.6f}")

    # Write all results to the output file
    with open(output_file_path, 'w') as output_file:
        for result in results:
            output_file.write(result + "\n")

# Execute the function
solve()
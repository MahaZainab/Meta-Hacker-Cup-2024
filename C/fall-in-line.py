import mmap
import time

start = time.time()

def points_not_on_line(points):
    if len(points) < 3:
        return len(points)

    dict = {}
    for b in points:
        for a in points:
            if a == b:
                continue

            k = a[0] - b[0]
            if k == 0:
                f = (a[0],)
            else:
                ax = (a[1] - b[1]) / k
                bb = (a[0]*b[1] - a[1]*b[0]) / k
                f = (ax, bb)

            if f not in dict:
                dict[f] = set()
            dict[f].add(tuple(a))
    on_line = max(len(v) for k, v in dict.items())
    print(len(points) - on_line)
    return len(points) - on_line

def process_file_mmap(filename):
    results = []
    
    with open(filename, 'r') as file:
        # Memory-map the file, size 0 means whole file
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            # Read number of test cases
            T = int(mmap_obj.readline().strip())
            
            for _ in range(T):
                # Read N for the current test case
                N = int(mmap_obj.readline().strip())
                
                # Read the points for each test case
                points = []
                for _ in range(N):
                    # Read the next line, split, and map to integers
                    line = mmap_obj.readline().strip().decode('utf-8')
                    x, y = map(int, line.split())
                    points.append((x, y))
                
                # Process the points and get the output
                output = points_not_on_line(points)
                results.append(output)
    
    # Print all results
    for i in range(1, len(results) + 1):
        print(f"Case #{i}: {results[i - 1]}")

# File with the input data
# filename = "input.txt"
filename = "fall_in_line_sample_input.txt"
process_file_mmap(filename)

end = time.time()

print("Time Taken = ", end - start, " seconds")
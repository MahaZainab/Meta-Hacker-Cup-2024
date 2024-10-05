def can_deliver_with_speed(speed, stations):
    for i, (a, b) in enumerate(stations):
        time_to_reach = (i + 1) / speed
        if not (a <= time_to_reach <= b):
            return False
    return True

def solve():
    T = int(input())  
    results = []
    
    for t in range(1, T + 1):
        N = int(input()) 
        stations = []
        for _ in range(N):
            A, B = map(int, input().split())
            stations.append((A, B))
        
        low, high = 0.000001, 10**6  
        precision = 1e-7  
        answer = -1
        
        while high - low > precision:
            mid = (low + high) / 2
            if can_deliver_with_speed(mid, stations):
                answer = mid
                high = mid
            else:
                low = mid
        
        if answer == -1:
            results.append(f"Case #{t}: -1")
        else:
            results.append(f"Case #{t}: {answer:.6f}")
    
    print("\n".join(results))

solve()

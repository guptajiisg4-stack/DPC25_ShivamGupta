def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
    
    for i in range(n-1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    leaders.reverse()
    return leaders

arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", findLeaders(arr))

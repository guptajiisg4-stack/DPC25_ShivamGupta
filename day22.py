from collections import Counter

def first_element_to_repeat_k_times(arr, k):
    freq = Counter(arr)
    
    for num in arr:
        if freq[num] == k:
            return num
    
    return -1

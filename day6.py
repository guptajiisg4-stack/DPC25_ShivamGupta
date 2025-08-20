from collections import defaultdict

def findZeroSumSubarrays(arr):
    prefix_sum = 0
    hashmap = defaultdict(list)  # stores indices where each prefix_sum occurs
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        hashmap[prefix_sum].append(i)

    return result

import math

def merge(arr1, arr2, m, n):
    gap = math.ceil((m + n) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8

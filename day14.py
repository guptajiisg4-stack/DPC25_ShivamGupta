def countSubstringsWithExactlyKDistinct(s: str, k: int) -> int:
    def atMostK(k: int) -> int:
        freq = {}
        left = 0
        total = 0
        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            total += (right - left + 1)
        return total

    if k > len(s):
        return 0
    return atMostK(k) - atMostK(k - 1)

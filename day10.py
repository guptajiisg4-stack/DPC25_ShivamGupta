from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    
    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())

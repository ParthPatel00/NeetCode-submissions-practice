class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sig = signature(word)
            anagram_map[sig].append(word)
        
        return list(anagram_map.values())
    
def signature(word: str) -> tuple:
    sig = [0] * 26

    for letter in word:
        sig[ord(letter) - ord('a')] += 1
    
    return tuple(sig)
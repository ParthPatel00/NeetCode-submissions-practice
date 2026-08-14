from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            signature = createSignature(s)
            groups[signature].append(s)
        
        return list(groups.values())


    

def createSignature(string: str) -> Tuple:
    tup = [0] * 26
    for char in string:
        tup[ord(char) - ord('a')] += 1
    
    return tuple(tup)



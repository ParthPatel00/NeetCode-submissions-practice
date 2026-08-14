from collections import Counter, defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        s_count = countElements(s)
        t_count = countElements(t)

        return s_count == t_count
    

def countElements(string: str) -> Dict:
        count = {}
        for char in string:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        return count


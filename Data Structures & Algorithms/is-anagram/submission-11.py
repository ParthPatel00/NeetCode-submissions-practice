class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        signature = []
        for word in [s, t]:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            signature.append(arr)

        return tuple(signature[0]) == tuple(signature[1])

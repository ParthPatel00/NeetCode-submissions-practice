class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = len(strs[0])
        pre = strs[0]
        for i in range(1, len(strs)):
            min_len = min(longest_prefix, len(strs[i]))
            while not pre[:min_len] == strs[i][:min_len]:
                min_len -= 1
            longest_prefix = min_len
            pre = strs[i][:min_len]
        
        return pre


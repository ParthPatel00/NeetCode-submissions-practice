class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 1
        for num in num_set:
            if num - 1 in num_set:
                continue
            count = 1
            curr_num = num
            while curr_num + 1 in num_set:
                count += 1
                curr_num += 1
            
            longest = max(longest, count)
        
        return longest
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = defaultdict()
        for i,n in enumerate(nums):
            complement = target - n
            if complement in pair:
                return [pair[complement], i]
            
            pair[n] = i

        return []

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix = 24
        postfix = 48
        nums = [1, 2, 4, 6]
        result = [48, 24, 12, 8]
        """
        n = len(nums)
        result = [1] * n
        prefix = 1

        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
        
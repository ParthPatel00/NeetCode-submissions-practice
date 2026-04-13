class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for color in nums:
            count[color] += 1
        
        j = 0
        for i,c in enumerate(count):
            nums[j:j+c] = [i]* c
            j = j + c
        
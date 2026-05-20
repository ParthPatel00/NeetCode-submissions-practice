class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6,7,8], k = 5
        [4,5,6,7,8,1,2,3]
        [8,7,6,5,4,3,2,1]
        """
        k = k % len(nums)
        nums.reverse()

        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

        
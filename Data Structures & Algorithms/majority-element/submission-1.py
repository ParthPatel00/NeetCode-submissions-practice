class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_freq = 1
        majority_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == majority_num:
                majority_freq += 1
            else:
                majority_freq -= 1

                if majority_freq == -1:
                    majority_freq = 1
                    majority_num = nums[i]
        
        return majority_num
            
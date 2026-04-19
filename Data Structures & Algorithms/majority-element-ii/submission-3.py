class Solution:    
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        target = len(nums) // 3
        for c in [candidate1, candidate2]:
            if c is not None and nums.count(c) > target:
                result.append(c)
        return result
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}

        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates[nums[i]] = [i]
            else:
                # check
                if i - duplicates[nums[i]][-1] <= k:
                    return True
                else:
                    duplicates[nums[i]].append(i)
        
        return False

        
                
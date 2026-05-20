class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,2,3,5,6,8] limit 8
        # candidate = (2,6)
        people.sort()

        l, r = 0, len(people) - 1
        num_boats = 0
        while l <= r:
            if l == r:
                num_boats += 1
                break
            if people[r] + people[l] > limit:
                # Need to take this solo person
                num_boats += 1
                r -= 1
            else:
                num_boats += 1
                r -= 1
                l += 1
        
        return num_boats
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        seen = {}

        for i, value in enumerate(nums):
            diff = target - value

            if diff in seen:
                coo = [seen[diff],i]
                return coo

            seen[value] = i
        

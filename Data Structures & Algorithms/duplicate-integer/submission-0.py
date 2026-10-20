class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        duplicates = set()
        for i in range(len(nums)):
            current=nums[i]
            if current in duplicates:
                return True
            else:
                duplicates.add(current)
        
        return False
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        l_prod = 1
        for i in range(n):
            res[i] = l_prod
            l_prod *= nums[i]
            
        r_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r_prod
            r_prod *= nums[i]
            
        return res
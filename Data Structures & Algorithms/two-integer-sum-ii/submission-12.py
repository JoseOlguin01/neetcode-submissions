class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = len(numbers)
        i = 0
        end = l - 1

        while i < end:

            if numbers[i] + numbers[end] == target:
                res = [i+1,end+1]
                return sorted(res)
            elif numbers[i] + numbers[end] > target:
                end -= 1
            elif numbers[i] + numbers[end] < target:
                i += 1
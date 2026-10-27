class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [char.lower() for char in s if char.isalnum()]

        length = len(clean)
        flag = 0
        end = length - 1
        res = 0
        while flag < length:

            if clean[flag] == clean[end]:
                res += 1
            flag += 1
            end -= 1

        if res == length:
            return True
        else:
            return False
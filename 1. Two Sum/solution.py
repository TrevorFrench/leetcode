class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        while i < len(nums):
            x = i + 1
            while x < len(nums):
                test = nums[i] + nums[x]
                if test == target:
                    break
                x = x + 1
            if test == target:
                break
            i = i + 1
        output = [i, x]
        return output
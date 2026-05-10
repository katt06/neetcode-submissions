class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        meow = {}
        
        for i, value in enumerate(nums):
            # diff = target - value
            diff = target - value
            if diff in meow:
                return [meow[diff], i]
            meow[value] = i



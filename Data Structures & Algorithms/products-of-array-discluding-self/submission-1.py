class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            prod = 1
            # we aren't looping back around
            for k in range(len(nums)):
                if(k != i):
                    prod *= nums[k]
            output.append(prod)
        return output
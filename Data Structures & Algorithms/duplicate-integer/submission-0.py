class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if the set of seen nums is smaller than the og, than the og has duplicates
        return len(set(nums)) < len(nums)
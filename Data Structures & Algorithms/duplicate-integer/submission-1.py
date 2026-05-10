class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # size is len(nums).
        seenSet = set()

        for n in nums:
            #check
            if n in seenSet:
                return True
            #put n in hashmap
            seenSet.add(n)
        return False
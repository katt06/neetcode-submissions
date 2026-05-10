class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap
        indices = {}

        for i, n in enumerate(nums):
            #adding all of nums to indicies
            #hashmap looks like {n, i} with n as the key
            indices[n] = i

        
        for i, n in enumerate(nums):
            """
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            """

            #difference is like nums[j]
            difference = target - n;

            if difference in indices and indices[difference] != i:
                return [i, indices[difference]]
    



        

            
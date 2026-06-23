class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #  nums[j] + nums[k] = -num[k]]
        #sort them, treating -num[k] as the target like in two sum
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #start
            left = i + 1
            
            #end
            right = len(nums) - 1

            while(left < right) :
                # target = -(nums[i])
                cursum = nums[i] + nums[left] + nums[right]
                if(cursum < 0):
                    left += 1
                
                elif(cursum > 0):
                    right -= 1
                
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

            
        return result

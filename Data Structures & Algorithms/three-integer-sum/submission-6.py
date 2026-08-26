class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i, a in enumerate(nums):
            #check if a is positive, that means there can never be three numbers that make 0
            if a > 0:
                break
            #skip duplicates since we need unique three elements
            if i > 0 and a == nums[i - 1]:
                continue

            #left is the one next to a and right is last element
            left, right = i + 1, len(nums) - 1

            while left < right:

                current_sum = a + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    #since there can be multiple answers
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result

        

        


        
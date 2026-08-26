class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #how is this diff from sliding window
        #is numbers sorted always
        answer_array = []

        #watch for index1 and index2 cannot be equals (tho that is probably accounted for in left < right)
        left, right = 0, len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return [left+1, right+1]

        return []
            
                
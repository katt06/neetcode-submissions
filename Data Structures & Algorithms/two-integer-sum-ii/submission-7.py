class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

    
        #using pointers
        # start 
        leftptr = 0
        #end
        rightptr = len(numbers) - 1 

        #this logic works since the array is sorted 
        #and the answer will be two numbers next to each other
        while leftptr < rightptr:
            currentSum = numbers[leftptr] + numbers[rightptr]
            if currentSum > target:
                rightptr -= 1
            elif currentSum < target:
                leftptr += 1
            elif currentSum == target:
                return [leftptr + 1, rightptr + 1]

        return []
        

        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        #set default number here
        result = [0] * n #full array of -1
        stack = [] #pairs [temp, index]

        for i, value in enumerate(temperatures):
            #temperatures[i] == value
            #want to compare to previous num (which was saved in the stack)
            while stack and value > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                #find index diff
                #use result[stackIndex] for correct placement for recently popped item
                result[stackIndex] = (i - stackIndex)

            stack.append([value, i])

        return result

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need the widest and tallest hmm
        #compare against the current bar
        #area = height[i] * i

        area = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                current = abs(min(heights[j], heights[i]) * (j - i))
                if current > area:
                    area = current
            
        return area
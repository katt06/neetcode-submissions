class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict should be key mapping to count
        counts = dict()

        #assigned counts
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        
        result = []
        for yay in range(k):
            max_key = max(counts, key = counts.get)
            result.append(max_key)

            del counts[max_key]

            
        return result


        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

    
        mapNum = defaultdict(int)
        for i in range(len(numbers)):
            check = target - numbers[i]
            if mapNum[check]:
                return [mapNum[check], i+1]
            mapNum[numbers[i]] = i + 1

        return []

        
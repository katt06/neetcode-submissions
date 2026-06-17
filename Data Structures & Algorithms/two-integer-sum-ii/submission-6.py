class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

    
        mapNum = defaultdict(int)
        for i in range(len(numbers)):
            check = target - numbers[i]
            # checking if that index for mapNum[check] is there
            if mapNum[check]:
                # outputs the index and the index above
                return [mapNum[check], i+1]
            # maps the number to its index + 1
            mapNum[numbers[i]] = i + 1

        return []

        
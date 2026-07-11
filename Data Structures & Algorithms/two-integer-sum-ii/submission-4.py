class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
                n = len(numbers)
                i= 0
                j= i+1

                for i in range(0,n-1):
                        j= i+1
                        while j<n:
                                if numbers[i] + numbers[j] == target:
                                        return [i+1, j+1]
                                j+=1
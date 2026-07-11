class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            n= len(numbers)
            temp= {}
            for i in range(0,n):
                remaining= target- numbers[i]
                if remaining in temp:
                    return [temp[remaining]+1, i+1]
                else:
                    temp[numbers[i]]=i
                            
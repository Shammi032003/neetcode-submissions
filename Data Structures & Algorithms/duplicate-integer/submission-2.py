class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp= []
        n= len(nums)
        for i in range(0,n):
            if nums[i] in temp:
                return True
            temp.append(nums[i])

        return False


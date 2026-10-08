class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        temp= {}
        for i in range(0,n):
            if nums[i] in temp:
                return True
            else:
                temp[nums[i]]=1
        
        return False
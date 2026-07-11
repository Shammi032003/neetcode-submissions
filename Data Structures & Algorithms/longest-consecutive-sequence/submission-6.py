class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp= []
        nums= set(nums)
        nums= sorted(nums)
        n= len(nums)
        count=1 
        max_count=1
        if nums== []:
            return 0
        for i in range(n-1):
            if nums[i+1]- nums[i] ==1:
                count+=1
                max_count= max(max_count, count)
            else:
                count=1

        return max_count
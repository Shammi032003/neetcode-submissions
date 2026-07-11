class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp= []
        n= len(nums)
        for i in range(0,n):
            prod= 1
            for j in range(0,i):
                prod= prod*nums[j]
            
            for j in range(i+1,n):
                prod= prod*nums[j]
                
            temp.append(prod)
            
        return temp
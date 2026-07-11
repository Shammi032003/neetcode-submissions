class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        temp= set()
        nums= sorted(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+ nums[j]+ nums[k]==0:
                        temp.add((nums[i], nums[j], nums[k]))
                        print(temp)           
        
        temp= list(temp)
        return temp
            

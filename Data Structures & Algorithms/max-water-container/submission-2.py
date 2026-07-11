class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        h= heights
        length = 0
        width= 0
        a=0

        for i in range(0,n):
            for j in range(i+1,n):
                if j>0:
                    width= j-i
                    length= min(heights[i], heights[j])

                    area= width*length

                    a= max(a, area)
                    j+=1
        return a






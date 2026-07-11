class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        h= heights
        length = 0
        width= 0
        i=0
        j= n-1
        a= 0
        l= heights[i]
        r= heights[j]
        while i<j:
            area= min(l,r)*(j-i)
            a= max(a,area)
            if l<r:
                i+=1
                l= heights[i]
            else:
                j-=1
                r= heights[j]
            
        return a
                






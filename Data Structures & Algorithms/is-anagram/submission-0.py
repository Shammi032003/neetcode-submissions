class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1= {}
        temp2= {}
        for i in s:
            if i in temp1:
                temp1[i]+=1
            else:
                temp1[i]=1
        
        print(temp1)
        
        for j in t:
            if j in temp2:
                temp2[j]+=1
            else:
                temp2[j]=1
        
        print(temp2)
        
        if temp1 == temp2:
            return True
        else:
            return False
        



        
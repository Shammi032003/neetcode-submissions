class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp2= {}
        for i in strs:
            temp1= {}
            for j in i:
                if j in temp1:
                    temp1[j]+=1
                else:
                    temp1[j]=1
        
            key= tuple(sorted(temp1.items()))
            
            if key in temp2:
                temp2[key].append(i)
            else:
                temp2[key]=[i]
    
        return list(temp2.values())
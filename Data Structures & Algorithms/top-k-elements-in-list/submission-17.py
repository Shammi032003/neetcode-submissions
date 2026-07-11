class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp= {}
        temp1= []
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]= 1
        
        print(temp)

        # Repeat k times
        for _ in range(k):
            max_value = max(temp.values())
        
            for key in temp:
                if temp[key] == max_value:
                    temp1.append(key)
                    del temp[key]
                    break   # important
    
        return temp1
            
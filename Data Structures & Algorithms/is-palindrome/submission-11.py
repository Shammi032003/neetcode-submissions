class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp= ""
        n= len(s)
        if s== " ":
            return True
        s= s.strip()
        s= s.lower()
        for i in range(0,n):
            if s[i].isalnum():
                temp+=s[i]
        print(temp)

        return temp== temp[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list()
        n=len(s)
        
        for i in range(n):
            if s[i].isalnum():
                if s[i].isupper():
                    l.append(s[i].lower())
                else:
                    l.append(s[i])
                
        if l==l[::-1]:
            return True
        else:
            return False
class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n==1:
            return False
        
        stack=[]
        for i in range(n):
            if len(stack)==0 or s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            elif s[i]==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i]=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                if stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append(s[i])
                    
        if len(stack)==0:
            return True
        else:
            return False
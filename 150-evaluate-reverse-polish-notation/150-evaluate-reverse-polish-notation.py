class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for i in range(n):
            if tokens[i]=="+":
                r=stack.pop()
                l=stack.pop()
                stack.append(l+r)
            elif tokens[i]=="-":
                r=stack.pop()
                l=stack.pop()
                stack.append(l-r)
            elif tokens[i]=="*":
                r=stack.pop()
                l=stack.pop()
                stack.append(l*r)
            elif tokens[i]=="/":
                r=stack.pop()
                l=stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(tokens[i]))
                
        return stack.pop()
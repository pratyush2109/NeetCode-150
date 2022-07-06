#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        st=[]
        for i in S:
            if i=="+":
                r=st.pop()
                l=st.pop()
                st.append(l+r)
            elif i=="-":
                r=st.pop()
                l=st.pop()
                st.append(l-r)
            elif i=="*":
                r=st.pop()
                l=st.pop()
                st.append(l*r)
            elif i=="/":
                r=st.pop()
                l=st.pop()
                st.append(l//r)
            else:
                st.append(int(i))

        return st[-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends
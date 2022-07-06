
#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        n=len(x)
        if n%2!=0:
            return False
            
        if n==0:
            return True
            
        st=list()
        for i in x:
            if len(st)==0 or i=="{" or i=="(" or i=="[":
                st.append(i)
            elif i=="}":
                if st[-1]=="{":
                    st.pop()
                else:
                    st.append(i)
            elif i==")":
                if st[-1]=="(":
                    st.pop()
                else:
                    st.append(i)
            else:
                if st[-1]=="[":
                    st.pop()
                else:
                    st.append(i)
                    
        if len(st)==0:
            return True
        else:
            return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


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
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
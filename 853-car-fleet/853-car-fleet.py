class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=[(position[i],speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        stack=[]
        fleet=0
        
        for pos,speed in arr:
            curr_time_taken=(target-pos)/speed
            
            if len(stack)==0 or curr_time_taken>stack[-1]:
                stack.append(curr_time_taken)
                fleet+=1
                
        return fleet
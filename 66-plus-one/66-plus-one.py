class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        n=int("".join(digits))
        n+=1
        n=str(n)
        digits=list(n)
        digits=[int(i) for i in digits]
        return digits
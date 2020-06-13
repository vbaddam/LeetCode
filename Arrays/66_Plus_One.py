class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(1,len(digits)+1):
            num = num + digits[-i]*10**(i-1)
        digits = [val for val in str(num+1)]
        return digits
        

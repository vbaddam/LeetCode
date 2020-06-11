class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0
        for num in nums:
            if num == 0:
                r = r + 1
            elif num == 1:
                w = w + 1
            else:
                b = b + 1
        
        nums[:r] = [0]*r
        nums[r:r+w] = [1]*w
        nums[r+w:] = [2]*b
        

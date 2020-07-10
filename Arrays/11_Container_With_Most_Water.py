class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        a = []
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                a.append(min(height[i],height[j])*(j-i))
        return(max(a))
        '''
        a = []
        i = 0
        
        j = len(height) - 1
        while i != j:
            a.append(min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return(max(a))
            
        #a = [min(height[i],height[j])*(j-i) for i in range(len(height)) for j in range(i+1, len(height))]
        #b = [height[j]*(j-i) for i in range(len(height)) for j in range(i+1, len(height))  if height[i] > height[j]]
        
    
       

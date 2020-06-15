class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        p = []
        for i in range(len(seats)):
            u = []
            if seats[i] == 0:
                for j in range(i+1, len(seats)):
                    if seats[j] == 1:
                        y = abs(j-i)
                        u.append(y)
                        
                        #print(y)
                        break
                for k in range(i-1, -1, -1):
                    if seats[k] == 1:
                        z = abs(k-i)
                        #print(z)
                        u.append(z)
                        break
                p.append(min(u))
       
        return(max(p))
                
                
        

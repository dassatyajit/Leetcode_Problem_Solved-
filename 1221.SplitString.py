class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        R_count=0
        L_count=0
        for i in s:
            if i=='L':
                L_count+=1
            else:
                R_count+=1
            if L_count==R_count:
                count+=1
                L_count,R_count=0,0      
        return count
                    
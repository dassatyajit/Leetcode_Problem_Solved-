class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max1:
                candies[i]=True 
            else:
                    candies[i]=False
        return candies
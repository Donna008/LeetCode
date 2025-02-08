# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # maxCandies = max(candies)
        # result = []
        # for c in candies:
        #     if c + extraCandies >= maxCandies:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        result=[]
        for i in candies:
            if i + extraCandies >= maxcandies:
                result.append(True)
            else:
                result.append(False)
        return result








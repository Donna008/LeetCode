# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         length = len(flowerbed)
        # i = 0

        # while i < length:
        #     if flowerbed[i] == 0:
        #         left_empty = (i==0) or (flowerbed[i-1]==0)
        #         right_empty = (i==length - 1) or (flowerbed[i+1]==0)
                
        #         if left_empty and right_empty:
        #             flowerbed[i]==1
        #             n -= 1
        #             if n <= 0:
        #                 return True
        #             i += 2
        #             continue
        #     i += 1
        # return n <= 0

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # length = len(flowerbed)
        # num=[]
        # for i in range(len(flowerbed)):
        #     if flowerbed[i]==0 and flowerbed[i]-1== 0 and flowerbed[i]+1 ==0:
        #         num.append(flowerbed[i])
        #     if n> len(num):
        #         return False
        #     else:
        #         return True
        length = len(flowerbed)
        count = 0
        for i in range(length):
            if flowerbed[i] == 0:
                left = (i ==0 or flowerbed[i-1]==0)
                right =(i==length-1 or flowerbed[i+1]==0)
                if left and right:
                    flowerbed[i]=1
                    count+=1
                    if count >=n:
                        return True
        return count>=n


             





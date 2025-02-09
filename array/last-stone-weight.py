class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) > 1:
        #     y = max(stones)
        #     stones.remove(y)
        #     if stones:
        #         x=max(stones)
        #         stones.remove(x)
        #         if x !=y:
        #             stones.append(y-x)
        # if stones:
        #     return stones[0]
        # else:
        #     return 0          
        # return stones[0] if stones else 0
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y!=x:
                heapq.heappush(stones,-(x-y))
        if stones:
            return stones[0]
        else:
            return 0
  
        
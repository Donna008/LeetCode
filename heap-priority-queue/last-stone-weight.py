class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)
            if stones:
                x=max(stones)
                stones.remove(x)
                if x !=y:
                    stones.append(y-x)
                   
        return stones[0] if stones else 0
                #     if num!=num2:
                #         sotones.append(num2 -num)
                # if stones:
                #     return stones[0]
                # else:
                #     return 0
        
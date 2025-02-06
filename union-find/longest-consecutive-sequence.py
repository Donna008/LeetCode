class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        hashset=set(nums)
        for num in hashset:
            if num-1 not in hashset:
                length =1
                next_num = num + 1
                while next_num in hashset:
                    length+=1
                    next_num += 1
                max_length=max(max_length,length)
        return max_length
        # max_length = 0
        # chars = set(nums)
        # for num in chars:
        #     length = 1
        #     next_num = num + 1
        #     while next_num in chars:
        #         length +=1
        #         next_num +=1
        #     max_length = max(max_length, length)
        # return max_length
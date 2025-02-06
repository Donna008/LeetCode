class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        for num in nums:
            if num-1 not in nums:
                length =1
                next_num = num + 1
                while next_num in nums:
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
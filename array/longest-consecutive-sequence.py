class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        chars = set(nums)
        # j=0
        for num in chars:
            length = 1
            next_num = num + 1
            while next_num in chars:
                length +=1
                next_num +=1
            max_length = max(max_length, length)
        return max_length
        #     while j in range(len(nums)):
        #         if nums[j] in chars:
        #             con = nums[j] +1
        #         chars.add(nums[i])
        #         max_length = max(max_length,j-i+1)
        # return max_length
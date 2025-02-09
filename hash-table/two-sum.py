class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one list nums, one target number
        # task two numbers = target
        #  find first num
        # for i in range(len(nums)):
        #     # find second one
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # hashmap
        #  make an empty map
        # map = {}
        # for i, num in enumerate(nums):
        #     value = target - num
        #     if value in map:
        #         return [map[value],i]
        #     map[num] = i
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]
                
        


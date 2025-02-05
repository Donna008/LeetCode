class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one list nums, one target number
        # task two numbers = target
        #  find first num
        for i in range(len(nums)):
            # find second one
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


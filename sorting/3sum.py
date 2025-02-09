# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        # found = {}
        # for i in range(0, len(nums)-2):
        #     seen = {}
        #     for j in range(i+1, len(nums)):
        #         needed = - nums[i] - nums[j]
        #         if needed in seen:
        #             result = [nums[i], nums[j], needed]
        #             result.sort()
        #             key = str(result[0]) + "." + str(result[1]) + "." + str(result[2])
        #             found[key] = result
        #         seen[nums[j]] = True
        #     pass
        # pass
        # ret = []
        # for key in found.keys():
        #     ret.append(found[key])
        # return ret


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        t=[nums[i],nums[j],nums[k]]
                        if t not in result:
                            result.append(t)
        return result
        # result=[]
        # found=[]
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] !=nums[j] or nums[i] != nums[k] and nums[j] != nums[k]:
        #                 nums[i]+nums[j]+nums[k]==0
        #                 found.append([nums[i],nums[j],nums[k]])
        #                 for i,j, k in found:
        #                     result.append([i,j,k])


        #                     # result.append([nums[i])
        # return result




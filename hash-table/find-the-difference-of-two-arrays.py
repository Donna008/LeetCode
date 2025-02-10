# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # set1, set2 = set(nums1),set(nums2)
        # return [list(set1 - set2),list(set2 - set1)]

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2=set(nums2)
        diff1 =list(nums1 - nums2)
        diff2 = list(nums2-nums1)
        return [diff1,diff2]




class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        # write = 0

        # for read in range(len(nums)):
        #     if nums[read] != 0:
        #         nums[write] = nums[read]
        #         write += 1

        # for i in range(write, len(nums)):
        #     nums[i] = 0
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero = []
        # non_zero= []
        # i = 0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         zero.append(nums[i])
        #         print(zero)
        #         i +=1
        #         # zero1=zero
        #     else:
        #         non_zero.append(nums[i])
        #         print(non_zero)
        #         # nozero=non_zero

        # name = non_zero+zero 
        # print(name)  
        # return name
        """
    #     Do not return anything, modify nums in-place instead.
    #     """
        non_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero]=nums[i]
                non_zero+=1
        for i in range(non_zero,len(nums)):
            # if nums[i]==0:
                nums[i]=0
               




# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)  # Creates a dictionary {num: frequency}
        
        # # Step 2: Use a heap to get the k most frequent elements
        # return heapq.nlargest(k, count.keys(), key=count.get)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_list=[]
        v=set()
        for i in range(len(nums)):
            if nums[i] in v:
                continue
            count=0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                   count+=1
            n_list.append((nums[i],count))
            v.add(nums[i])
        n_list.sort(key=lambda x: -x[1])
        result = []
        for i in range(k):
            result.append(n_list[i][0])
        return result

            

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)  # Creates a dictionary {num: frequency}
        
        # # Step 2: Use a heap to get the k most frequent elements
        # return heapq.nlargest(k, count.keys(), key=count.get)


        # brute force
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         n_list=[]
#         v=set()
#         for i in range(len(nums)):
#             if nums[i] in v:
#                 continue
#             count=0
#             for j in range(len(nums)):
#                 if nums[i] == nums[j]:
#                    count+=1
#             n_list.append((nums[i],count))
#             v.add(nums[i])
#         n_list.sort(key=lambda x: -x[1])
#         result = []
#         for i in range(k):
#             result.append(n_list[i][0])
#         return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        freq_map=Counter(nums)         
        heap=[]
        result=[]
        for num, freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
        # while head:
            if len(heap)>k:
                heapq.heappop(heap)
        for freq, num in heap:
            result.append(num)
        return result







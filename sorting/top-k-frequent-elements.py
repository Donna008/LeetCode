class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Creates a dictionary {num: frequency}
        
        # Step 2: Use a heap to get the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)
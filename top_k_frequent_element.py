# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from heapq import heappush, heappop

def topKFrequent(nums, k):
    # create a hashmap that keeps track of each element and its frequency {1:3, 2:2, 3:1}
    # return the top k keys with highest values
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    # create a min heap
    min_heap = []
    for num, freq in hashmap.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)
    top_k_frequent = [pair[1] for pair in min_heap]
    return top_k_frequent



nums = [1,1,1,2,2,3]
k = 2
topKFrequent(nums, k)
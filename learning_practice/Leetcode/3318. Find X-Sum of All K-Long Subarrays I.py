from collections import Counter
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer  = []
        for i in range(n - k + 1):
            subarray = nums[i : i+ k]
            freq = Counter(subarray)
            top_element = sorted(freq.items(), key = lambda p:(-p[1], -p[0]))
            top_x = set([val for val, cnt in top_element[:x]])
            total = sum(num for num in subarray if num in top_x)
            answer.append(total)
        return answer
        
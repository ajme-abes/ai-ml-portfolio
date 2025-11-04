class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        current_index = 0
        n = len(colors)
      
        while current_index < n:
            # Start of a new group
            group_start = current_index
            group_sum = 0
            max_time = 0
          
            while current_index < n and colors[current_index] == colors[group_start]:
                group_sum += neededTime[current_index]
                if max_time < neededTime[current_index]:
                    max_time = neededTime[current_index]
                current_index += 1
            if current_index - group_start > 1:
                total_cost += group_sum - max_time
      
        return total_cost

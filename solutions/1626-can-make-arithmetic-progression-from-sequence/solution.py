# Iteration 2
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ordered_arr: List[int] = sorted(arr)
        common_difference = None
        for i in range(1, len(ordered_arr), 1):
            difference = ordered_arr[i] - ordered_arr[i-1]
            if common_difference is None:
                common_difference = difference
            elif difference != common_difference:
                return False
        return True

# Iteration 1
# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         ordered_arr = sorted(arr)
#         common_difference = None
#         for i in range(1, len(ordered_arr), 1):
#             difference = ordered_arr[i] - ordered_arr[i - 1]
#             print(difference)
#             print("CD is num: ", common_difference is not None)
#             print("Difference Match: ", difference != common_difference)
#             if (common_difference is not None) and (difference != common_difference):
#                 return False
#             common_difference = difference
#         return True


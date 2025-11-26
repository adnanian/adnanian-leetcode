# Iteration 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # All negative numbers will be false
        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True
        # Rest by converting an int to a string
        str_num = str(x)
        left_index = 0
        right_index = len(str_num) - 1
        mid_index = len(str_num) / 2
        while left_index <= mid_index and right_index >= mid_index:
            if str_num[left_index] != str_num[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True

# Iteration 1
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # By converting an int to a string
#         str_num = str(x)
#         left_index = 0
#         right_index = len(str_num) - 1
#         mid_index = len(str_num) / 2
#         while left_index <= mid_index and right_index >= mid_index:
#             print("L: ", left_index)
#             print("R: ", right_index)
#             if str_num[left_index] != str_num[right_index]:
#                 return False
#             left_index += 1
#             right_index -= 1
#         return True


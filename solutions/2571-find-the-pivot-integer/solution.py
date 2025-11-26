# Iteration 1
class Solution:
    def pivotInteger(self, n: int) -> int:
        # Sum of 1 to n is a triangular number
        sum_of_n: int = n * (n + 1) / 2
        for i in range(1, n + 1, 1):
            # Simply compare the difference between triangular numbers
            left_sum = int(i *(i + 1) / 2)
            right_sum = int(sum_of_n - ((i - 1) * i / 2))
            # print("Left Sum: ", left_sum)
            # print("Right Sum: ", right_sum)
            if left_sum == right_sum:
                return i
        return -1

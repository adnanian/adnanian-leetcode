from math import ceil

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        factorial: int = 1
        nums: List[int] = [1]
        # Compute factorial
        for i in range(2,n):
            factorial *= i
            nums.append(i)
        nums.append(n)
        permutation: str = ""
        new_k = k
        print(f"n={n}, k={k},f={factorial}")
        while len(nums):
            if len(nums) > 1:
                # Subtract one since it's 0-index
                block_index = ceil(new_k / factorial) -1
                print(block_index)
                permutation += str(nums.pop(block_index))
                new_k = new_k - (block_index * factorial)
                factorial /= len(nums)
                # print(f"NewK={new_k}")
                # print(f"Perm={permutation}")
                # print(f"Fact={factorial}")
            else:
                permutation += str(nums.pop(0))
        return permutation

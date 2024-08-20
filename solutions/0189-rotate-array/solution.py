class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        original_nums = nums[:]
        for i in range(len(nums)):
            k_index = (i + k) % len(nums)
            nums[k_index] = original_nums[i]

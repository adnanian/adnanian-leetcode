class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_index: int = len(nums) - 1
        # print("Start SI: ", swap_index)
        index: int = 0
        while index <= swap_index:
            # When index > swap_index, element is "_"
            if nums[index] == val:
                nums[index] = nums[swap_index]
                nums[swap_index] = "_"
                swap_index -= 1
                # Decrement swap_index to show next last num.
            else:
                # Only increment index if there is no swap.
                index += 1
        # print("End SI: ", swap_index)
        # print(swap_index + 1)
        return swap_index + 1

        

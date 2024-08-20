class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}
        for num in nums:
            if duplicate_map.get(str(num)) == num:
                return True
            else:
                duplicate_map[str(num)] = num
        return False
        

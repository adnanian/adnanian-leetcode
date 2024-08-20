class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map = {}
        for num in nums:
            if not num_map.get(str(num)):
                num_map[str(num)] = 1
            else:
                num_map[str(num)] += 1
        for (key, value) in num_map.items():
            if num_map[key] == 1:
                print(num_map[key])
                return int(key)

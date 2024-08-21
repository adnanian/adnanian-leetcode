class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {}
        # Nums 1
        for num in nums1:
            if not num_map.get(str(num)):
                num_map[str(num)] = [1, 0]
            else:
                num_map[str(num)][0] += 1
        # Nums 2
        for num in nums2:
            if not num_map.get(str(num)):
                num_map[str(num)] = [0, 1]
            else:
                num_map[str(num)][1] += 1
        # Intersection
        intersection = []
        for (key, value) in num_map.items():
            if 0 not in value:
                intersection += [int(key)] * min(value)
        return intersection
                

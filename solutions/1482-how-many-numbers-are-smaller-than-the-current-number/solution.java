class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        // Initialize array of zeros for return value.
        int[] smallers = new int[nums.length];
        // Loop through array for each element to count the number of smallers.
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                if (nums[i] > nums[j]) {
                    smallers[i]++;
                }
            }
        }
        return smallers;
    }
}

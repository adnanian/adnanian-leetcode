// Iteration 2
class Solution {
    public int[] getConcatenation(int[] nums) {
        // Step #1 - Create a new array of length 2n.
        int[] ans = new int[nums.length * 2];
        // Step #2 - Copy the nums array to ans at index 0.
        System.arraycopy(nums, 0, ans, 0, nums.length);
        // Step #3 - Copy the nums array again to ans, this time at index nums.length.
        System.arraycopy(nums, 0, ans, nums.length, nums.length);
        // Step #4 - Return the duplicated array.
        return ans;
    }
}

// Iteration 1
// class Solution {
//     public int[] getConcatenation(int[] nums) {
//         int[] ans = new int[nums.length * 2];
//         for (int i = 0; i < nums.length; i++) {
//             ans[i] = nums[i];
//             ans[i + nums.length] = nums[i];
//         }
//         return ans;
//     }
// }

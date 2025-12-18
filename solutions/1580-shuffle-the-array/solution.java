class Solution {
    public int[] shuffle(int[] nums, int n) {
        // Create a new array of length 2n (nums.length)
        int[] shuffledArr = new int[nums.length];
        // i = split index for left and right sides of num array.
        // j = index of the shuffledArr array
        for (int i = 0, j = 0; i < n && j < shuffledArr.length; i++, j += 2) {
            // First j-index, add the i-index of left side.
            shuffledArr[j] = nums[i];
            // Second j-index, add the i-index of the right side.
            shuffledArr[j + 1] = nums[i + n];
        }
        return shuffledArr;
    }
}

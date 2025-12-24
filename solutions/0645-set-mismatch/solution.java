// Iteration #2
class Solution {
    public int[] findErrorNums(int[] nums) {
        // Initialize empty array of size nums.length (asc);
        int[] numSet = new int[nums.length];

        // Initialize duplicate.
        // Then loop through nums.
        int duplicate = 0;
        int j = 0; // numSetIndex
        for (int i = 0;i<nums.length;i++) {
            int num = nums[i];
            j = num - 1;
            if (numSet[j] == num) {
                duplicate = num;
            } else {
                numSet[j] = num;
            }
        }
        
        // Loop through numSet to find missingNum
        int missingNum = 0;
        j = 0;
        while (missingNum == 0 && j < numSet.length) {
            if (numSet[j] == 0) {
                missingNum = j + 1;
            }
            j++;
        }

        return new int[]{duplicate,missingNum};
    }
}

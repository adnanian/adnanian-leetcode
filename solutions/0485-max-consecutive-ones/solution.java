class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        // Current max number of consecutive 1's.
        int maxStreak = 0;
        // Current number of consecutive 1's in the iteration process.
        int currentStreak = 0;
        for (int num: nums) {
            currentStreak = (num == 1) ? currentStreak + 1 : 0;
            maxStreak = Math.max(maxStreak, currentStreak);
        }

        return maxStreak;
    }
}

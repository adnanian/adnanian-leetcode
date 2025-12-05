class Solution {
    public boolean isPowerOfTwo(int n) {
        // All non-positive numbers will return false,
        // since it's impossible for a positive exponential
        // relationship to reach 0 or below.
        if (n <= 0) {
            return false;
        }
        double power = Math.log(n) / Math.log(2);
        return Math.pow(2, Math.floor(power)) == n;
    }
}

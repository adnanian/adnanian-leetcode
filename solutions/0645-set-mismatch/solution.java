import java.util.ArrayList;

class Solution {
    public int[] findErrorNums(int[] nums) {
        // Initialize list of sorted numbers from 1 to n (asc);
        ArrayList<Integer> numList = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            numList.add(i + 1);
        }
        // Initialize duplicate.
        // Then loop through nums.
        int duplicate = 0;
        for (int num: nums) {
            if (numList.contains(num)) {
                // Pop nums from numList.
                numList.remove(Integer.valueOf(num));
            } else {
                // Set the duplicate if num is already removed.
                duplicate = num;
            }
        }
        // Missing num is the remaining num in numList.
        int missingNum = !numList.isEmpty() ? numList.get(0) : 0;
        return new int[] {duplicate, missingNum};
    }
}

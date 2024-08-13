/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = function(nums) {
    console.log(nums);
    for (let i = 0; i < nums.length - 1; i++) {
        let j = i + 1;
        while (j < nums.length) {
            if (nums[i] === nums[j]) {
                nums.splice(j,1);
            } else {
                j++;
            }
        }
    }
    console.log(nums);
    return nums.length;
};

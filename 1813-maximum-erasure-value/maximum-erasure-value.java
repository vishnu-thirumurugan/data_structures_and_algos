class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int left = 0;
        int maxSum = 0;
        int currSum = 0;

        for (int right = 0; right < nums.length; right++){
            while (seen.contains(nums[right])){
                seen.remove(nums[left]);
                currSum -= nums[left];
                left++;
            }
            seen.add(nums[right]);
            currSum += nums[right];
            maxSum = Math.max(maxSum, currSum);

        }
        return maxSum;
    }
}
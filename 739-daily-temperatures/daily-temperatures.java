class Solution {
    public int[] dailyTemperatures(int[] nums) {
        int[] answer = new int[nums.length];
        Stack <Integer> stack = new Stack<>();

        for (int i = nums.length-1; i >= 0; i--){
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]){
                stack.pop();
            }
            answer[i] = stack.isEmpty() ? 0:stack.peek()-i;
            stack.push(i);
        }
        return answer;
    }
}
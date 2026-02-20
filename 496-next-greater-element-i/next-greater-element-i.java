class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> nextGreater = new HashMap<>();
        Stack <Integer> stack = new Stack<>();

        // find the next greater element in nums2
        for (int i = nums2.length-1;i >=0;i--){
            while (!stack.isEmpty() && stack.peek() < nums2[i]){
                stack.pop();
            }
            nextGreater.put(nums2[i], stack.isEmpty() ? -1:stack.peek() );

            stack.push(nums2[i]);

        }

        // form the answer from the dict based on the order from nums1
        int ans[] = new int[nums1.length];
        for (int i = 0; i < nums1.length;i++){
            ans[i] = nextGreater.get(nums1[i]);
        }
        return ans;

    }
}
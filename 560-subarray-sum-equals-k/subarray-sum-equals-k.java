class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int prefix_sum = 0;
        int res = 0;

        map.put(0,1);

        for (int i = 0; i < nums.length; i++){
            prefix_sum += nums[i];

            if (map.containsKey(prefix_sum-k)){
                res += map.get(prefix_sum-k);
            }

            map.put(prefix_sum, map.getOrDefault(prefix_sum,0)+1);

        }

        return res;
    }
}
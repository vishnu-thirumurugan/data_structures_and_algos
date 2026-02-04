class Solution {
    public int lengthOfLongestSubstring(String s) {
        // sliding window approach
        int left = 0;
        int max_len = 0;

        for(int right=0; right < s.length(); right++){
            // move left until the current character is present in window
            while (s.substring(left, right).contains(String.valueOf(s.charAt(right)))){
                left += 1;
            }

            max_len = Math.max(max_len,right-left+1);
        }

        return max_len;
        
    }
}
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++){
            while (s.substring(left,right).contains(String.valueOf(s.charAt(right)))){
                left += 1;
            }
            maxLength = Math.max(maxLength, right-left+1);
        }
        return maxLength;
        
    }
}
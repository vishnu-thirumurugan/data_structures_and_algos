class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        // for this we have to start the pointers from the end and start editing the nums1
        int i = m-1;
        int j = n-1;
        int k = m+n-1; // len of final array --> start filling from this position

        while (i >= 0 & j >= 0){
            if (nums2[j] > nums1[i]){
                nums1[k] = nums2[j];
                j--;
                k--;
            }
            else{
                nums1[k] = nums1[i];
                i--;
                k--;
            }
        }

        // if there are remanining elements in nums2
        while (j >= 0){
            nums1[k] = nums2[j];
            j--;
            k--;
        }
        
    }
}
class Solution {
    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        int maxi = -1;
        for (int i = n-1; i > -1; i--){
            int temp = arr[i];
            arr[i] = maxi;
            maxi = Math.max(temp, maxi);
        }

        return arr;
    }
}
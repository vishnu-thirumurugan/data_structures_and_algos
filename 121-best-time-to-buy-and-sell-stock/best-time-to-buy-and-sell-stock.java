class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int maxProfit = 0;

        for (int p : prices){
            if (p < buyPrice){
                buyPrice = p;
            }

            maxProfit = Math.max(maxProfit, p - buyPrice);
        }
        return maxProfit;
    }
}
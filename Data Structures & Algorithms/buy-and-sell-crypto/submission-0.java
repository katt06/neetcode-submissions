class Solution {
    public int maxProfit(int[] prices) {
        int maxValue = 0;
        for( int i = 0; i < prices.length; i++){
            for( int j = (prices.length - 1); j > i; j--){
                int k = prices[j] - prices[i];
                if(k > maxValue){
                    maxValue = k;
                }

            }
        }
        return maxValue;
    }
}

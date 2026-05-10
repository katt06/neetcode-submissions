class Solution {
    public int longestConsecutive(int[] nums) {

        //gotta start noticinng the patterns,
        //so lets focus on finding the start of sequemces
        //start of sequences are only valid if num - 1 doesn't exist in the array
        //with the stat of a sequence, start counting

        int longestStreak = 0;
    
        HashSet<Integer> copy = new HashSet<>();

        // use enhanced loop
        for (int num : nums){
            copy.add(num);
        }

        for (int num : nums){
            
            //if prev sequence does exist, then skip counting so it only counts for starts
            if (copy.contains(num - 1)) continue;

            int currentNum = num; //have to make a copy to increment
            int streak = 1;

            //mini iteration for the starter
            while(copy.contains(currentNum + 1)){
                streak++;
                currentNum++;
            }

            longestStreak = Math.max(streak, longestStreak);


        }
        return longestStreak;
        
    }
}

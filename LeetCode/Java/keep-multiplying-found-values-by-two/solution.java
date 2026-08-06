class Solution {
    public int findFinalValue(int[] nums, int original) {
        int max = 1001;
       boolean[] hmap = new boolean[max];
       for(int i=0; i<nums.length; i++){
            hmap[nums[i]]=true;
       }
       while(original < max && hmap[original]){
        original = 2 * original;
       }
       return original;
    }
}
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
    ArrayList<Boolean> ans = new ArrayList<>(); 
    int value = 0;
     for(int i=0; i<nums.length; i++){
        value =(value*2 +nums[i])%5;
        ans.add(value == 0);
        }
     return ans; 
    }
}
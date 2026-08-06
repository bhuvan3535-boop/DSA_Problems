class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        boolean[] arr = new boolean[nums.length + 1];
        List<Integer> result = new ArrayList<>();
        for(int num : nums){
            arr[num] = true;
        }
        for(int i=1; i<arr.length; i++){
            if(arr[i] != true){
                result.add(i);
            }
        }
        return result;
    }
}
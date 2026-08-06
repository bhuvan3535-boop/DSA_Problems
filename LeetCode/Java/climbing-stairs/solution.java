class Solution {
    public int climbStairs(int n) {
        int[] arr = new int[n];
        int i=2;
        if(n < 3){
            return n;
        }
        while(i< n){
            arr[0] = 1;
            arr[1] = 2;
            arr[i] = arr[i-1] + arr[i-2];
            i++;    
        }
        return arr[n-1];
        }
    }

public class upperbound {
    // {
    // // public int upperBound(int[] nums, int x) {
    // //         for(int i =0;i<nums.length;i++){
    // //             if(nums[i]>x){
    // //                 return i;
    // //             }
    // //         }
    // //         return nums.length;
    // // }

    public int upperBound(int[] nums, int x){
        int n = nums.length;
        int low =0, high = n;
        while(low<high){
            int mid = low +(high-low) /2;
            if(nums[mid] >x){
                n = mid;
                high = mid;
            }
            else{
                low = mid+1;
            }
        }
        return n;
    }
}



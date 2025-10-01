class Solution {
    //public int lowerBound(int[] nums, int x) {
    //   for(int i =0;i<nums.length;i++){
    //     if(nums[i]>=x) return i;
    //   } 
    //   return nums.length;
    //  }
     public int lowerBound(int[] nums, int x) {
       int low =0,high = nums.length;
       int ans = 0;
       while(low<=high){
        int mid = low +(high-low) /2;
    //     if(nums[mid] == x){
    //         ans = mid;
    //         high = mid;
    //     }
    //     else if(nums[mid] >x){
    //         ans = mid;
    //         high = mid-1;
    //     }
    //     else{
    //         low = mid+1;
    //     }
    //    }
    //    return ans;

    if(nums[mid] < x){
        low = mid+1;
    }
    else{high = mid;}

       }
       return low
     }
}

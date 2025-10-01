public class Solution {
  public int[] getFloorAndCeil(int[] nums, int x) {
    // int[] fc = new int[2];
    // int n = nums.length;
    // for (int i = 0; i < nums.length; i++) {
    //   if (nums[i] == x) {
    //     fc[0] = x;
    //     fc[1] = x;
    //     return fc;
    //   }
    //   if (nums[i] > x) {
    //     fc[1] = nums[i];
    //     if (i > 0) {
    //       fc[0] = nums[i - 1];
    //     }
    //     return fc;
    //   }
    // }
    // if(x>nums[n-1]){
    //     fc[0] = nums[n-1];
    // }
    // return fc;
    int low =0, high = nums.length;
    while(low<high){
        int mid = low+(high-low)/2;
        if(nums[mid]==x){
            int[] ans = {x,x};
            return ans;
        }
        if(nums[mid]>x){
            high = mid;
        }
        else{
            low = mid+1;
        }
    }
    int [] ans = new int[2];
    ans[0] = low>0?nums[low-1]:-1;
    ans[1] = low<nums.length?nums[low]:-1;
    
    return ans;
  }

  }

 
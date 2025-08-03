class Solution {
    public int search(int[] nums, int target) {
         int size = nums.length;
         int left =0; int right = size-1;
        // int mid = (right+left)/2;
         while(left<=right){
            int mid = (right+left)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]<target)  left = mid+1;
            if(nums[mid]>target ) right = mid-1;
         }
         return -1;
    }
}
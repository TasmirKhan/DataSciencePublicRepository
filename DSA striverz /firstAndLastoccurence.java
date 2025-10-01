public class firstAndLastoccurence {
    public int[] searchRange(int[] nums, int target) {
    //     int start =-1,end = -1;
    // for(int i=0;i<nums.length;i++){
    //    if(nums[i] ==target && start == -1){
    //     start = i;
    //    }
    //    if(nums[nums.length-1-i] == target && end == -1){
    //     end = nums.length-1-i;
    //    }
    // }
    // if(end==-1){end = start;}
    // return new int[]{start,end};
       int fo=-1,lo =-1;
    int low =0,high = nums.length-1;
    while(low<=high){
        int mid = low +(high-low)/2;
        if(nums[mid]== target){
            fo = mid;
            high = mid-1;
        }
        else if(nums[mid] > target){
            high = mid-1;
        }
        else{
            low = mid+1;
        }

    }

    low =0,high = nums.length-1;
    while(low<=high){
        int mid = low+(high-low)/2;
        if(nums[mid]== target){
            lo = mid;
            low = mid+1;
        }
        else if(nums[mid] > target){
            high = mid-1;
        }
        else{
            low = mid+1;
        }
        
    }
    return new int[]{fo,lo};

    }
} 


public class lowerbound {

    public static int iterativeLowerBound(){
    int []nums = {2, 4, 6, 8, 10, 12, 14};
     int x = 9;
    
     for(int i =0;i<nums.length;i++){
        if(nums[i]>=x){
            return i;
        }        
     }
     return -1;
}
    public static int binarylowerbound(int[]arr,int target){
        int low =0, high = arr.length-1;
        int key =0;
        while(low<=high){
           int mid = low+(high-low)/2;
            if(arr[mid]==target)return mid;
            else if(arr[mid]<target) low = mid+1;
            else high = mid - 1; key = mid;


        }
      return key;
    }
    public static void main(String[] args) {
        int [] arr = {1,2,3,5,6,7,7,9,11,13};
         int z = iterativeLowerBound();
         System.err.println(z);
         System.out.println(binarylowerbound(arr, z));
    }
}
     
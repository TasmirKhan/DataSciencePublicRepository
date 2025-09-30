public class searchInsert {
    public static int iterativeSearchInsert(int[]arr,int x){
        
        for(int i =0;i<arr.length;i++){
            if(arr[i]>x ) return i;
        }
        return arr.length;
    }

    public static int binarySearchInsert(int[] arr,int x){
        int low =0, high =arr.length-1;  
        while(low <=high){
            int mid = low + (high-low)/2;
            if(arr[mid] == x) return mid;
            else if(arr[mid]<x) {low = mid+1;}
            else if(arr[mid]>x){
                high  = mid -1;
            }
        }

        return low;
    }
    public static void main(String[] args) {
        int [] arr = {1,2,3,4,5,6,7,8,9,11,12,13,14,15};
        int x =10;
        System.out.println(iterativeSearchInsert(arr, x));
        System.out.println(binarySearchInsert(arr, x));
    }
}

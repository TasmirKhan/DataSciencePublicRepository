import java.util.Scanner;

public class upperBound {

    public static int iterativeupperBound(int[]arr,int x){
        for(int i=arr.length-1;i>=0;i--){
            if(arr[i]<=x){
                return i;
            }
        }
        return -1;
    }

    public static int binaryUpperBound(int[]arr,int x){
        int low =0,high =arr.length-1;
        int ans =-1;
        while(low<=high){
            int mid = low +(high-low)/2;
            if(arr[mid] == x) return mid;
            else if(arr[mid] < x){
                ans = mid;
                low  = mid +1;
            }
            else{
                high = mid -1;
            }
        }
        return ans;
    }
    public static void main(String[] args){
        int [] arr = {1,2,3,4,5,6,7,8,9,11,21,23};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the required number.");
        int x = sc.nextInt();
        int y = iterativeupperBound(arr, x);
        System.err.println(y);
        int z = binaryUpperBound(arr, y);
        System.err.println(z );

    }
}

import java.util.Arrays;
import java.util.Scanner;

public class sample1 {
    public static void main(String[] args) {
        System.out.println("Here is our first sample problem.");
//         Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Our task is to find these two numbers.
// Input
// [2, 3, 2, 1, 5]
// Output
// 4 2
        System.out.println("Enter the length of the Array.");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int[] arr2 ={2,3,2,1,5};
        Arrays.sort(arr2);
       // System.out.println(Arrays.toString(arr2));
        for(int i=0;i<arr2.length;i++){
            if(arr[i]>i+1){
                missing = i
            }
        }

    }
}

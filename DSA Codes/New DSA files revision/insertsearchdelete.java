import java.util.Scanner;

public class insertsearchdelete{

   public static void search(int[] arr,int x){
        for(int i=0;i<arr.length;i++){
            if(arr[i] == x){
                System.out.println("index of the given integer in the array is "+i);
                return ;
            }
            
        }
      System.out.println("Element not found");
    }

    public static void insert(int[]arr, int x){
        int[] arr1 = new int[arr.length-1];
        int j=0;
        


    }
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. to be found");
        int a = sc.nextInt();
        search(arr,a);
    }
}
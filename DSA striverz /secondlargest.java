import java.util.Arrays;
public class secondlargest{
    public static void sl(int[]arr){
         Arrays.sort(arr);
        System.out.println(arr[arr.length-2]);
        return; 
    }
    public static void main(String[] args) {
        int[]arr  = {1,2,3,4,32,4,53,2,4,5,3,2,4};
        sl(arr);
    }
}

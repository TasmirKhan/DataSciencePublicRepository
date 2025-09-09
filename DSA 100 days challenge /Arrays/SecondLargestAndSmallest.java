package Arrays;

import java.util.Arrays;

public class SecondLargestAndSmallest {

    public static void directOrBruteForce(int []arr){
        Arrays.sort(arr);
        System.out.println("Second largest : "+arr[arr.length-2]+" ,Second smallest: "+arr[1]);
    }
    
    public static void manual(int [] arr){
        for(int i=0;i<arr.length;i++){
            0
        }
    }
    // public static void Manual
    public static void main(String[] args) {
        int []arr = {1,3,42,4,2,4,2,6,2,65,7,3,6,843,6};
        directOrBruteForce(arr);


    }
}

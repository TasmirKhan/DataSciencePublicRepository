import java.util.*;

public class arraycombine{
    public static void main(String[] args) {
        System.err.println("Array combination");
        int [] arr1 = {1,2,3,4,5};
        int [] arr2 = {23,12,34,12,234};
        // method 1
        int [] newarr = new int[arr1.length+arr2.length];
        for(int i=0;i<arr1.length;i++){
            newarr[i]= arr1[i];
        }
        for(int i=0;i<arr2.length;i++){
            newarr[(arr1.length)+i] = arr2[i];
        }
        System.out.println("New array is "+Arrays.toString(newarr));

    }
}
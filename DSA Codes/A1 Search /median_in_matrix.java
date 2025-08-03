import java.util.Arrays;

public class median_in_matrix {

    
public static int binaryMedian(int[][] arr,int r,int c){
     int[] flattenedArray = Arrays.stream(arr).flatMapToInt(Arrays::stream).toArray();
     Arrays.sort(flattenedArray);
     int n = flattenedArray.length;
     int median = flattenedArray[n/2];
     return median;
    
}

    public static void main(String [] args){
        int r = 3, c = 3;
        int m[][]= { {1,3,5}, {2,6,9}, {3,6,9} };
        
        System.out.println("Median is " + binaryMedian(m, r, c));
    }
}


public class copyarray{
    public static void main(String[] args){
        int[] arr={1,2,3,4,5,6};
        int[] copyarray = new int[arr.length];
        // for (int i=0;i<arr.length;i++) {
        //     copyarray[i] = arr[i];
        // }

        // Another approach
        System.arraycopy(arr, 0, copyarray, 0, arr.length);
    }
}
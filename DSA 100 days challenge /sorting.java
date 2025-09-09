

public class sorting {

    public static void insertionSort(int[] arr){
    
    }

    public static void selectionSort(int[] arr){
        for(int i =0;i<arr.length; i++){
            int mini = arr[i];
            for(int j=0;j<arr.length;j++){
                if(arr[i])
            }
        }
    }

    public static void bubbleSort(int[] arr){

    }
    public static void main(String[] args) {
        sorting s = new sorting();
        int [] arr = {1,2,3,4,2,3,1,2,43,5,32,2,4,5,3,2,43,5};
        int [] arr2 = {4,4,3,2,5,8,4,3,6,8,4,3,5,87,9,4,2,4,6,4,9};
        int [] arr3 = {1,2,42,7,1,3,2,4,5,3,6,8,6,8,9,7,5,3,7,8};
        s.insertionSort(arr);
        s.selectionSort(arr2);
        s.bubbleSort(arr3);

        
    }
}

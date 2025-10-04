public class rotationOfArray {
    public static int main(String[] args) {
        
    
    int []arr = {4,5,6,7,0,1,2,3};
    int low =0, high= arr.length;
    while(low<=high){
        int mid = low+(high-low)/2;
        if(arr[mid]>arr[high]){
            low = mid+1;
        }
        else{
            high = mid;
        }
        
    }
    return low;
}
}
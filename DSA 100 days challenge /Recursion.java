import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.concurrent.ArrayBlockingQueue;
import java .util.ArrayList;
public class Recursion {

    public void Recurse(String x,int a){
        if(a==5) return ;
        System.out.println(x);
        a++;
        Recurse(x,a);
    }

    public void RecName(String x, int n){
        if(n==0) return;
        System.out.println(x);
        n--;
        RecName(x, n);
    }

    public void PrintNumber(int n,int i){
      if(n==0) return ;
      System.out.print(i+" ");
      i++;
      n--;
      PrintNumber(n,i);
    }

    public void PrintRevNumber(int n){
        if(n==0) return;
        System.out.print(n+" ");
        n--;
        PrintRevNumber(n);
    }

    public void sumOfN(int n, int sum){
        
        if(n==0) {System.out.println(sum); return;}
        
        sumOfN(n-1,sum+n);
    }

    public void Factorial(int n, int Fact){
        
        if(n==0) {System.out.println(Fact); return;}
        
        Factorial(n-1,Fact*n);
    }

    public int factOfN(int n){
        if(n==0){
            
            return 1;
        }
        return n*factOfN(n-1);
    }

    public static void reversArray(int[] arr, int x){
        int i =0;
        while(i<arr.length){
            if(i<arr.length/2){
                int a = arr[i];
                int b = arr[arr.length -i-1];
                arr[i] = b;
                arr[arr.length-i-1] = a;
                          }
                            i++;
        }
        System.out.println(Arrays.toString(arr));

    }

    public static void revarrrec(int[] arr,int start,int end){
        if(start>=end) return;
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp ;
        revarrrec(arr, start+1, end-1);
        System.out.println(Arrays.toString(arr));
    }

    public static boolean stringPalindrome(String s, int start, int end){
        s = s.toLowerCase();
        if(start >= end) return true;
        if(s.charAt(start) != s.charAt(end)) return false;
        return stringPalindrome(s, start+1, end-1);
    }

    public static void fibonacci(int n ){
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(0);arr.add(1);arr.add(1);
        for(int i = arr.size()-1;i<=n;i++){
            arr.add(arr.get(i)+arr.get(i-1));
        }
        System.out.println(arr);
    }
    public static void main(String[] args) {
        Recursion r = new Recursion();
        r.Recurse("Tasmir Khan", 0);
        r.RecName("Mr.Tasmir khan", 5);
        r.PrintRevNumber(10);
        System.out.println();
        r.PrintNumber(10,1);
        System.out.println();
        r.sumOfN(10,0);
        System.out.println(r.factOfN(5));
        r.Factorial(6,1);


        int[] arr = {12,23,34,45,56,67,78,89,90};
        System.out.println(Arrays.toString(arr));
        reversArray(arr, arr.length);
        
        int[] arr1 = {1,2,3,4,5};
        revarrrec(arr1, 0, arr1.length-1);
        String s = "MalayalaM";
        boolean x = stringPalindrome(s, 0, s.length()-1);
        System.out.println(x);
        fibonacci(5);

    }
}

// import java.util.*;
// import java.lang.Math;
// public class nthroot {
//     public static void main(String[] args) {
//         System.out.println("Enter the number: ");
//         Scanner sc = new Scanner(System.in);
//         int m = sc.nextInt();
//         int n = sc.nextInt();
//         int ans =0;
//         // for(int i=0;i<m;i++){
//         //     if(Math.pow(i,n)==m){System.out.print(i) ;return ;}
//         //     if(Math.pow(i,n)<m) ans = i;
//         // }
//         int low =0, high =m;
//         while(low<=high){
//             int mid = (low+(high-low))/2;
//             if(Math.pow(mid,n)==m){
//                 System.out.println(mid);
//                 return ;
//             }
//             if(Math.pow(mid,n)>m){
//                 high = mid-1;
//             }
//             else{
//                 low = mid+1;
//             }
//         }
//         System.out.println(low);
//}}
import java.util.*;
import java.lang.Math;

public class nthroot {
    public static void main(String[] args) {
        System.out.println("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int ans = -1;

        int low = 0, high = m;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            double power = Math.pow(mid, n);

            if (Math.abs(power - m) < 1e-9) {  // to handle floating precision
                System.out.println(mid);
                sc.close();
                return;
            }

            if (power < m) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        System.out.println(ans); // print final answer
        sc.close();
    }
}

    
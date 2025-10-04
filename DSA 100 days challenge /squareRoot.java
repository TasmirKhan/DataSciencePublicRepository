import java.util.Scanner;
public class squareRoot {
    public static void main(String[] args) {
        System.out.println("Enter the number you want to find the squareRoot of ");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int low =0, high =x;
        while(low<high){
             int mid = (low+high)/2;
             int sq = mid*mid;
             if(sq==x){ System.err.println(mid); break;}
             else if(sq>x) high = mid-1;
             else low = mid+1;
        }
       System.err.println(low);
    }
}

import java.util.*;

public class trailingZeroesinfactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b =a;
        int temp = 1;
        // while(a!=0){
        //     temp = temp*a;
        //     a--;
        // }
        // System.out.println("Factorial of given number is = "+ temp);
        // int count=0;
        // while(temp%10==0){
        //     count++;
        //     temp = temp/10;
        // }
        // System.out.println("Trailing Zeroes in the factorial of given number is "+ count);

        int count2 = 0;
        for(int i=5;b/i>=1;i = i*5){
            count2 = count2+(b/i);
            }
        System.out.println("Trailing zeroes of given number using optimal approach is "+ count2);

    }
}

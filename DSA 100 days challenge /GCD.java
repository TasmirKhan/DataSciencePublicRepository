import java.math.BigInteger;
import java.util.Scanner;
import java.math.BigInteger;
public class GCD {

    public static int gcd(int a , int b){
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }

    public static int gcdwithBI(int a , int b){
        return BigInteger.valueOf(a).gcd(BigInteger.valueOf(b)).intValue();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = gcd(a,b);
        System.out.println("The GCD of "+a+" and "+b+" is "+c);
        System.out.println("The GCD by biginteger method is "+gcdwithBI(a,b));

        System.out.println("The LCM of given numbers is "+ ((a*b)/gcd(a, b)));
    }
}

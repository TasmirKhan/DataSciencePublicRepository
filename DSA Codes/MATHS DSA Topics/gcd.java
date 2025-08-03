
import java.util.Scanner;

public class gcd{

public static int Gcd(int a, int b){
    while(b!=0){
        int temp = b;
        b = a%b;
        a=temp;
    }
    return a;
}
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the two numbers to find the GCD of the two numbers.");
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println("Gcd of the given no. "+x+" and "+y+" is "+Gcd(x,y));
    }
}
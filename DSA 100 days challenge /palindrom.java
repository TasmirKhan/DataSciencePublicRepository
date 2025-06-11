
import java.util.*;
public class palindrom{
    public static void main(String[] args ){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        long a = sc.nextLong();
        long b =a;
        int length = Long.toString(Math.abs(a)).length();
        long temp =0;
        for(int i=0;i<length;i++){
            temp = (temp*10) + (a%10);
            a = a/10;
        }
        System.out.println("REverse of the given number is : "+ temp);
        if (temp == b) System.out.println("Palindrome");
        else System.out.println("Not Palindrome");
    }
}

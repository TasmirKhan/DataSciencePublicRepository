import java.util.Scanner;

public class palindrome {

    public static boolean isPalindrome(int a){
        if(a<0 || (a%10==0 && a!=0)) return false;
        int rh =0;
        while(a>rh){
        {  rh = rh*10 + (a%10);
            a = a/10;}
        
        }
        return  a==rh || a==(rh/10);
        //The two conditions is checked as we don't Know that whether the no. of digits in a is even or odd.
    }
    public static void main(String[] args) {
        System.out.println("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("The given no. is a Palindrome : "+isPalindrome(n));
    }
}

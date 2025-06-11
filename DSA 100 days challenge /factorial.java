import java.util.*;
public class factorial {
   public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter Your number: ");
    long a = sc.nextLong();
    long temp =1;
    while(a!=0){
        temp = temp*(a);
        a = a-1;
    }
    System.out.println("Factorial of the given number is : "+ temp);

   } 
}

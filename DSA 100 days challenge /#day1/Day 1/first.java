import java.util.*;
// count digits
public class first{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Your Number:-");
        long a = sc.nextLong();

        long temp = a;
        // counting the number of digits in a given number
        int count =0;
        // Using loops;
        while(a/10>0){
            a = a/10;
            count++;
            if(a>0 && a<10) count++;
        }
        System.out.println("Number of digits in the given number-> "+count);
    
        // Using Math.log10() method
        int count2 = (temp==0) ? 1:(int)(Math.log10(Math.abs(temp)))+1;
        System.out.println("Number of digits calculated using Math.log() method : "+count2);

    }
}
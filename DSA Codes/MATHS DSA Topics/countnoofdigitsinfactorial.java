import java.util.*;
public class countnoofdigitsinfactorial {

    static int countdigits(int n){
        if(n<0) return 0;
        if(n<=1) return 1;
        // double digits = 0;
        // for(int i=2;i<=n;i++){
        //     digits += Math.log10(i);
        // }
        // return (int)Math.floor(digits)+1;
        double pi = Math.PI;
        double e = Math.E;

        // Stirling's approximation formula
        double digits = (0.5 * Math.log10(2 * pi * n)) + 
                        (n * Math.log10(n / e));
        return (int)Math.floor(digits)+1;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
       
        System.out.println("The given no. of digits are given below.");  
         System.out.println(countdigits(n));
    }
}
import java.util.Scanner;


public class prime {


    public static void isprimeopt(int a){
        if(a<=1){
            System.out.println("Not Prime");
            return;
        }
        if(a==2 || a==3){
            System.out.println("Prime");
            return;
            }

        if(a%2==0 || a%3==0){
            System.out.println("Not Prime");
            return;
        }

         // check divisibility by numbers of form 6k ± 1
        for (int i = 5; i * i <= a; i += 6) {
            if (a % i == 0 || a % (i + 2) == 0) {
                System.out.println("Not Prime");
                return;
            }
        }

        System.out.println("Prime");
    }


    public static void isprime(int a){
    if(a==2){
        System.out.println("Prime");
        return;
    }
    for(int i=2;i<a;i++){
        if(a%i == 0){
            System.out.println("Non Prime"); return;
        }
    }
    System.out.println("Prime");
    }

    public static void main(String[] args){
        System.out.println("Enter Your number: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        isprime(a);
        
    }
}

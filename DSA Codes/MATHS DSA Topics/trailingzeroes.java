import java.util.Scanner;

public class trailingzeroes {

    public static int tz(int x){
        if(x<0) return -1;
        else if(x<5) return 0;
        int count =0;
        // This is the logic which reduces the time complexity of the program as well as the chances of overflow is avoided
        for(int i=5;x/i>=1;i=i*5){
            count = count+x/i;
        }
        return count;
    }
    public static void main(String[] args) {
        System.out.println("Enter the number whose factorial's trailing zeros you want to find.");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.println("The number of the trailing Zeroes in the "+x+" is "+tz(x) );
    }
}

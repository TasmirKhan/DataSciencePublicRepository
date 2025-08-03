import java.util.Scanner;

public class removedigitfromstring{
    public static void main(String[] args){
        System.out.println("Enter the String:");
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println("Original String = "+s);
        s = s.replaceAll("[0-9]", "");
        System.out.println("Updated = "+s);
    }
}
import java.util.*;

public class patterns{

    public static void box(int a){
        System.out.println("Box Pattern:");
             for(int i=a ;i>0;i--){
            for(int j=a;j>0;j--){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void leftTriangle(int a){
        System.out.println("Left Triangle");
        for(int i=0;i<a;i++){
            for(int j=0;j<=i;j++ ){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void leftNoTriangle(int a){
        for(int i=1;i<=a;i++){
            for(int j =1;j<=i;j++){
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public static void leftSameTriangle(int a){
        for(int i=1;i<=a;i++){
            for(int j =1;j<=i;j++){
                System.out.print(i);
            }
            System.out.println();
        }
    }

    
    public static void leftupsidedown(int a){
        for(int i=a;i>0;i--){
            for(int j =1;j<=i;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void upsidedownnumber(int a){
        for(int i=a;i>0;i--){
            for(int j=1;j<=i;j++){
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public static void triangle(int a){
        if(a%2==0) return;
        else{
            for(int i=0;i<a;i++){
                for(int j=0;j<a-i-1;j++){
                    System.out.print(" ");
                }
                for(int j=0;j<2*i+1;j++){
                    System.out.print("*");
                }
                for(int j=0;j<a-i-1;j++){
                    System.out.print(" ");
                }
                System.out.println();
            }
        }
    }
public static void invertTriangle(int N)  v
{
    // This is the outer loop which will loop for the rows.
    for (int i = 0; i < N; i++)
    {
        // For printing the spaces before stars in each row
        for (int j =0; j<i; j++)
        {
            System.out.print(" ");
        }
       
        // For printing the stars in each row
        for(int j=0;j< 2*N -(2*i +1);j++){
            
            System.out.print("*");
        }
        
        // For printing the spaces after the stars in each row
        for (int j =0; j<i; j++)
        {
            System.out.print(" ");
        }
       

        // As soon as the stars for each iteration are printed, we move to the
        // next row and give a line break otherwise all stars
        // would get printed in 1 line.
        System.out.println();
    }
}
    public static void main(String[] args){
        
        int n =3;
        box(n);
        leftTriangle(n);
        leftNoTriangle(n);
        leftSameTriangle(n);
        leftupsidedown(n);
        upsidedownnumber(n);
        triangle(n);
    }
}
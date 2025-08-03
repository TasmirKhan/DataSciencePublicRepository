import java.util.ArrayList;
import java.util.List;

public class feb18th{
    public static void main(String[] argv)
    { 

        // Creating object of ArrayList<Integer> 
        List<Integer> list1 = new ArrayList<Integer>(); 

        // Populating list1 
        list1.add(9); 
        list1.add(20); 
        list1.add(30); 

        // Creating another object of ArrayList<Integer> 
        List<Integer> list2 = new ArrayList<Integer>(); 
        
        // Populating list1 
        list2.add(10); 
        list2.add(20); 

        // Retains elements of list1 specified in list2 using retainAll() method 
        list1.retainAll(list2); 

        // print list1 
        System.out.println(list1); 
    } 
}
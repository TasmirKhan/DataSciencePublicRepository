public class count {

    public int counting(int n){
        if(n>0) n = n;
        else {n = Math.abs(n);}
        int a=0;
        while(n>0){
          n = n/10;
          a++;
        }
        return a;

    }
    public static void main(String[] args) {
        System.out.println("Main method entrance");
      count c = new count();
       int x = c.counting(-123);
   System.out.println(x);
   System.out.println("Alternate and more efficient way to find the number of elements in a number : "+(int)(Math.log10(123)+1));
    }
}

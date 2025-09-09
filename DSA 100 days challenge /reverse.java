public class reverse {
    public int doreverse(int x){
        int a = 0;
        while(x>0){
            a = a*10+x%10;
            x = x/10;
        }
        return a;
    }
    // public int optimalReverse(int a){

    // }
    public static void main(String[] args) {
        reverse r=new reverse();
        int a = r.doreverse(12345);
        System.out.println(a);
    }
}

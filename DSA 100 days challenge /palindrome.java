public class palindrome {
    public String dopal(int x){
        int c =x;
        
        int n =0;
        while(x>0){
            n = n*10+x%10;
            x = x/10;
        }
        if(c == n) return "yes";
        return "no";

        
    }

//     class Solution {
//     public boolean isPalindrome(int x) {
//         int rh =0;
//         while(x>rh){
//             rh = rh*10+x%10;
//             x = x/10;
//         }
//         return (x == rh || x==rh/10 );
//     }
// }
    public static void main(String[] args) {
        palindrome p = new palindrome();
        System.out.println(p.dopal(121));
    }
}

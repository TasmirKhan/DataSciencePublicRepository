public class Second {
  boolean isPalindrome(int a ){
    int x=0;
    while(a>0){
      int temp = a%10;
      x = x*10+temp;
      a = a/10;
      if(a==x){
        return true;
      }
    }
    
    return false;
 }

 int fact(int a){
  if(a==0 || a==1) return 1;
  int result =1;
  for(int i=1;i<=a;i++){
   result *=i;
  }
  return result;
 }

 int trailzero( int n ){
 int c=0;
  for(int i=5;n/i>=1;i=i*5){
    c = c+n/i;
  }
  return c;
 }

 int gcd(int a , int b){
  if(a==0) return b;
  if(b==0) return a;
  if(a>b)return gcd(b,a%b);
  return gcd(a,b%a);
 }

 int lcm(int a,int b){
     return (a*b)/(gcd(a,b));
 }

 boolean isprime(int a ){
  if(a<=1) return false;
  if(a==2 || a==3) return true;
  if(a%2==0 || a%3==0) return false;
  for(int i =5;i<Math.sqrt(a);i+=6){
    if(a%i==0 || a%(i+2)==0){
      return false;
    }
   
  }
  return true;
 }

 void divisor(int a ){
     for(int i=1;i<=a/2;i++){
      if(a%i==0) System.out.print(i+" ");
     }
 }
   public static void main(String[] args) {
       //Palindrome, Factorial, Trailing zeroes, Gcd or Hcf , Lcm, Check for prime , divisor.
      Second s = new Second();
       int a = 12;
       int b =34;
      System.out.println("Palindrome "+s.isPalindrome(a));
      System.out.println("factorial "+s.fact(a));
      System.out.println("no.of trialing zeores "+s.trailzero(a));
      System.out.println("gcd "+s.gcd(a, b));
      System.out.println("lcm "+s.lcm(a,b));
      System.out.println("prime or not -> "+s.isprime(a));
      // System.out.println(s.primefactor(b));
      s.divisor(b);


       
   } 
}

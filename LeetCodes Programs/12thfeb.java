// class Solution {
//     public int maximumSum(int[] nums) {
//         if(nums.length <=1) return -1;
//         int temp=0;
//         int maxx =0;
//         ArrayList<Integer> lst = new ArrayList<>();
//         for(int i=0;i<nums.length;i++){
//             temp =0;
//              int num = nums[i];
//             while(num>0){               
//                 temp = temp+num%10;
//                 num= num/10;
//             }
//             lst.add(temp);
//         }
//         for(int i=0;i<nums.length;i++){
//             for(int j=0;j<nums.length;j++){
//                 if(i!=j && lst.get(i)==lst.get(j)){
//                     maxx = Math.max(maxx, nums[i]+nums[j]);
//                 }
//             }
//         }
//         if(maxx==0) return -1;
//         return maxx;
//     }
// }
import java.util.HashMap;
import  java.util.Scanner;
class feb12th{
    public int maximumSum(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int maxSum = -1;

        for (int num : nums) {
            int digitSum = getDigitSum(num);
            if (map.containsKey(digitSum)) {
                maxSum = Math.max(maxSum, num + map.get(digitSum));
                map.put(digitSum, Math.max(map.get(digitSum), num)); // Store the max value
            } else {
                map.put(digitSum, num);
            }
        }
        return maxSum;
    }

    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
    public static void main(String[] args){
        System.out.println("Max sum of a pair with equal sum of digits");
        int[] arr = new int[5];
        System.out.println("Enter the five input integers of your array.");
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<arr.length;i++){
            try{
                arr[i] = sc.nextInt();
            }
            catch(Exception e){
                System.out.println("!Invalid Input "+e.getMessage());
                break;
            }
        }
        feb12th sol = new feb12th();
        System.out.println("Maximum sum = "+ sol.maximumSum(arr));              
    }
}

public class Solution10feb{
    public String clearDigits(String s) {
        StringBuilder sb = new StringBuilder(s);
        
        for (int i = 0; i < sb.length(); i++) {
            if (Character.isDigit(sb.charAt(i))) {
                // Find the closest non-digit character to the left
                int j = i - 1;
                while (j >= 0 && Character.isDigit(sb.charAt(j))) {
                    j--; // Skip over digits
                }
                
                if (j >= 0) {
                    sb.deleteCharAt(j); // Remove closest non-digit character
                    i--; // Adjust index after deletion
                }
                
                sb.deleteCharAt(i); // Remove the digit itself
                i--; // Adjust index after deletion
            }
        }

        return sb.toString();
    } {
    
}

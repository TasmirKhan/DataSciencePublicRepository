public class searchinRotatedSortedArray {
    
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                return mid; // Found target
            }

            // Check which side is sorted
            if (nums[low] <= nums[mid]) {
                // Left side sorted
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1; // Search left
                } else {
                    low = mid + 1;  // Search right
                }
            } else {
                // Right side sorted
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1; // Search right
                } else {
                    high = mid - 1; // Search left
                }
            }
        }

        return -1; // Not found
    }
}



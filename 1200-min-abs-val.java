import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
https://leetcode.com/problems/minimum-absolute-difference/submissions/

Stats: O(n*lgn) time, O(n) space -- 
    Runtime: 14 ms, faster than 98.69% of Java online submissions for Minimum Absolute Difference.
    Memory Usage: 50.1 MB, less than 86.35% of Java online submissions for Minimum Absolute Difference.

*/

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] sorted) {
        Arrays.sort(sorted);
        
        // one pass to find diff
        int minDiff = sorted[1] - sorted[0];
        List<List<Integer>> result = new ArrayList<>();
        for (int i=1; i<sorted.length; i++) {
            //found a smaller minDiff --> eviscerate clean return arr, calculate new minDiff
            if ((sorted[i] - sorted[i-1]) < minDiff) {
                minDiff = Math.min(minDiff, sorted[i] - sorted[i-1]);
                result.clear();
            }
            
            //find the new pair and add to result
            if ((sorted[i] - sorted[i-1]) <= minDiff) {
                List<Integer> pair = new ArrayList<>();
                pair.add(sorted[i-1]);
                pair.add(sorted[i]);
                result.add(pair);
            }
        }
        
        return result;
    }
}
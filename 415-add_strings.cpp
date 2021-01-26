class Solution {
public:
//     string addStrings(string num1, string num2) {        
//         int p1 = num1.size();
//         int p2 = num2.size();
              
//         string result = "";
//         bool carry = false;
        
//         while (p1 >= 0 || p2 >=0 || carry) {
//             int sum = 0;
            
//             if (p1 >= 0) {
//                 sum = sum + num1[p1] - '0';
//                 p1--;
//             }
            
//             if (p2 >= 0) {
//                 sum = sum + num1[p2] - '0';
//                 p2--;
//             }
            
//             if (sum + carry >= 10) {
//                 carry = true;
//                 sum = sum - 10;
//             }
//             else {
//                 carry = false;
//             }
            
//             result += to_string(sum);            
//         }
        
//         reverse(result.begin(), result.end());
//         return result;
//     }
    
    // not sure why my version above doesn't work; this solution is from
    // https://leetcode.com/problems/add-strings/discuss/501850/Easy-and-clean-code
    string addStrings(string num1, string num2) {        
        int idx1 = num1.size() - 1, idx2 = num2.size() - 1;
        int carry(0);
        string ans;

        while(idx1 > -1 || idx2 > -1 || carry) {
            int d1 = (idx1 >= 0) ? num1[idx1--] - '0' : 0;
            int d2 = (idx2 >= 0) ? num2[idx2--] - '0' : 0;
            int sum = d1 + d2 + carry;
            carry = sum/10;
            ans += '0' + (sum % 10);    // ans = sum%10 + '0' + ans; and no reverse
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
    
};

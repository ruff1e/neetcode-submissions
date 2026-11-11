class Solution {
    public boolean isPalindrome(String s) {
        

        /* 

            s = "WasitacaroracatIsaw"   // return: true

            s == [s::-1]


        */

        StringBuilder newStr = new StringBuilder();

        for(char c : s.toCharArray()) {
            if(Character.isLetterOrDigit(c)) {
                newStr.append(Character.toLowerCase(c));
            }
        }

        return newStr.toString().equals(newStr.reverse().toString());
        

    }
}

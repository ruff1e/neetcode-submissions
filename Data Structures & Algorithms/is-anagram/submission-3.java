class Solution {
    public boolean isAnagram(String s, String t) {


        /*

            s = "racecar", t = "carrace"        return: true
            s = "car"    t = "arc"              return: true

            s="", t=""                          return: false


            solution: hashmap

            countS, countT = {r:2, a:2, c:2, e:1}  {c:2, a:2, r:2, e:1}
            countS == countT : return : true
            o(n) + o(m) 

        */

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();

        for(int i=0; i<s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return countS.equals(countT);

    }
}

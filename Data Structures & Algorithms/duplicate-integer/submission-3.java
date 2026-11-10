class Solution {
    public boolean hasDuplicate(int[] nums) {
        

        // nums = [1, 2, 3, 3]
        // return True if there are duplicates

        // brute force: double loop


        // nums = [1, 2, 3, 3]
        //  time compx: o(n)^2             x, y,

        // nums = [1, 2, 3, 3]
        //
        // 
        //
        //
        //

        Set<Integer> seen = new HashSet();

        for(int num : nums) {
            if(seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;



    }
}
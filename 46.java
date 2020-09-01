class Solution {
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length == 1) {
            ArrayList<List<Integer>> a = new ArrayList<List<Integer>>();
            ArrayList<Integer> aa = new ArrayList<Integer>();
            aa.add(nums[0]);
            a.add(aa);
            return a;
        }
        ArrayList<List<Integer>> list = new ArrayList<List<Integer>>();
        for(int i = 0; i < nums.length; ++i) {
            // get permutations of every element but nums[i]
            int[] arr = new int[nums.length-1];
            int c = 0;
            for(int n : nums) {
                if(n != nums[i])
                    arr[c++] = n;
            }
            List<List<Integer>> l = permute(arr);
            for(List<Integer> ll : l) {
                ArrayList<Integer> a = new ArrayList<Integer>();
                a.add(nums[i]);
                for(int n : ll) {
                    a.add(n);
                }
                list.add(a);
            }
        }
        return list;
    }
}

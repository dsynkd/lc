class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(n == 0)
            return;
        if(m == 0) {
            nums1 = nums2;
            return;
        }
        int i = 0, j = 0;
        vector<int> v;
        while(i < m || j < n) {
            cout << i << "," << j << endl;
            if(j >= nums2.size() || (nums1[i] <= nums2[j] && i < m)) {
                v.push_back(nums1[i++]);
            }
            else {
                v.push_back(nums2[j++]); 
            }
        }
        nums1 = v;
    }
};

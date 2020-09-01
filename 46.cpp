class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if(nums.size() == 1) {
            vector<vector<int>> v = {{nums[0]}};
            return v;
        }
        vector<vector<int>> a;
        for(int i = 0; i < nums.size(); ++i) {
            vector<int> b;
            for(int j = 0; j < nums.size(); ++j) {
                if(j == i)
                    continue;
                b.push_back(nums[j]);
            }
            vector<vector<int>> c = permute(b);
            for(int j = 0; j < c.size(); ++j) {
                vector<int> p = c[j];
                vector<int> d = {nums[i]};
                for(int k = 0; k < p.size(); ++k)
                    d.push_back(p[k]);
                a.push_back(d);
            }
        }
        return a;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> buckets(n + 1);

        unordered_map<int, int> freq;
        vector<int> res;

        for (int num : nums) {
            if (freq.find(num) == freq.end()) {
                freq[num] = 1;
            } else {
                freq[num] += 1;
            }
        }
        for (const auto& key_val : freq) {
            buckets[key_val.second].push_back(key_val.first);
        }
        for (int i = n ; i >= 0 ; i--) {
            for(int curr: buckets[i]) {
                res.push_back(curr);
                k--;
                if (k == 0) {
                    return res;
                }
            }
        }
        return res;

    }
};

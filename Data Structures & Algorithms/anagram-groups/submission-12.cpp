class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        int n = strs.size();

        for (int i = 0 ; i < n ; i++) {
            vector<int> tmp(26, 0);
            for (char c : strs[i]) {
                tmp[c - 'a'] += 1;
            }
            string key = to_string(tmp[0]);
            for (int j = 1 ; j < 26 ; j++) {
                key += "," + to_string(tmp[j]);
            }
            groups[key].push_back(strs[i]);
        }
        vector<vector<string>> res;
        for (const auto& p: groups) {
            res.push_back(p.second);
        }
        return res;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> count(26, 0);

        for (size_t i = 0; i < s.size() ; i++) {
            count[s[i] - 'a'] += 1;
            count[t[i] - 'a'] -= 1;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};

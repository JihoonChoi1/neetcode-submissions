class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (const string& str : strs) {
            int n = str.length();
            res += to_string(n) + "#";
            res += str;
        }
        return res;
    }

    vector<string> decode(string s) {
        int n = s.length();
        int i = 0;
        vector<string> res;
        while (i < n) {
            string tmp = "";
            while (s[i] != '#') {
                tmp += s[i];
                i += 1;
            }
            i++;
            int currSize = stoi(tmp);
            tmp = "";
            while (currSize) {
                tmp += s[i];
                currSize -= 1;
                i += 1;
            }
            res.push_back(tmp);
        }
        return res;
    }
};

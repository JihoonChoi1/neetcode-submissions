class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dictionary;
        vector<int> res = {0, 0};

        for (size_t i = 0 ; i < nums.size() ; i++) {
            if (dictionary.count(target-nums[i])) {
                res[0] = dictionary[target-nums[i]];
                res[1] = i;
                return res;
            }
            dictionary[nums[i]] = i;
        }
        return res;

    }
};

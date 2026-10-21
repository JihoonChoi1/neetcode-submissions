class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> dictionary;

        for (int i = 0 ; i < n ; i++) {
            int diff = target - nums[i]; 
            if (dictionary.find(diff) != dictionary.end()) {
                return {dictionary[diff], i};
            }
            dictionary.insert({nums[i], i});
        }
        return {};

    }
};

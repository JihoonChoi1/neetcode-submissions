class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<size_t> visited;
        for (int i = 0 ; i < nums.size() ; i++) {
            if (visited.contains(nums[i])) {
                return true;
            }
            visited.insert(nums[i]);
        }
        return false;
    }
};
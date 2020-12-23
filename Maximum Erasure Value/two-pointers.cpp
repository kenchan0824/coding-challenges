#include <iostream>
#include <vector>
#include <numeric>
#include <unordered_set>
using namespace std;

int solution(vector<int>& nums) {
    int n = nums.size();
    vector<int> psum(n+1, 0); 
    partial_sum(nums.begin(), nums.end(), psum.begin()+1);
    
    unordered_set<int> queue;
    int i = 0, score = 0; 
    for(int j=0; j<n; j++) {
        while (queue.find(nums[j]) != queue.end()) {
            queue.erase(nums[i++]);
        }
        score = max(score, psum[j+1] - psum[i]);
        queue.insert(nums[j]);
    }
    return score;
}

int main() {

    // vector<int> nums = {4,2,4,5,6};
    // cout << solution(nums) << endl;

    vector<int> nums = {5,2,1,2,5,2,1,2,5};
    cout << solution(nums) << endl;
}

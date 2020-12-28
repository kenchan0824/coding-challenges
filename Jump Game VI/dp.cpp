#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> f(n, -INT32_MAX);
    f[0] = nums[0];
    for (int i=1; i<n; i++) {
        f[i] = *max_element(f.begin()+max(0,i-k), f.begin()+i) + nums[i];
    }
    return f[n-1];
}

int main() {
    vector<int> nums = {1,-1,-2,4,-7,3};
    int k = 2;
    cout << solution(nums, k) << endl;
}

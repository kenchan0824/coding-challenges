#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <numeric>
#include <chrono>
using namespace std;

int solution(vector<int> &A) 
{
    unordered_set<int> setA{A.begin(), A.end()};
    int maxA = *max_element(A.begin(), A.end());

    if (maxA < 1) return 1;

    for (int i=1; i <= maxA; i++)
    {
        if (setA.find(i) == setA.end()) return i;
    }

    return maxA + 1;
}

int main()
{
    //vector<int> A = {1, 3, 6, 4, 1, 2};
    vector<int> A(100000);
    iota(A.begin(), A.end(), 1);

    auto begin = std::chrono::high_resolution_clock::now();

    cout << solution(A) << endl;

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("elapsed %.4f seconds.\n", elapsed.count() * 1e-9);
}
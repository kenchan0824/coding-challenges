#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>        // max_element
#include <numeric>          // iota
#include <chrono>
using namespace std;
using namespace std::chrono;

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

    auto begin = high_resolution_clock::now();

    cout << solution(A) << endl;

    auto end = high_resolution_clock::now();
    auto elapsed = end - begin;
    printf("elapsed %.4f seconds.\n", elapsed.count() * 1e-9);
}
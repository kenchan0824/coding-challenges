#include <iostream>
#include <vector>
#include <random>       // rand
#include <algorithm>    // generate
#include <chrono>
using namespace std;
using namespace std::chrono;

vector<int> mem(1001, -1);

int recursion(const vector<int> &P, const int n)
{
    if (n == 1) return P[0];

    if (mem[n] != -1) return mem[n];

    int optimal = 0;
    for (int k=0; k<n; k++)
    {
        int remain = n - (k + 1);
        int profit = P[k] + recursion(P, remain);
        optimal = max(optimal, profit);
    }
    mem[n] = optimal;
    return optimal;
}

int tabular(const vector<int> &P, const int n)
{
    vector<int> table(n+1, 0);

    for (int l=1; l<=n; l++)
    {
        for (int k=0; k<l; k++)
        {
            int remain = l - (k + 1);
            table[l] = max(table[l], P[k] + table[remain]);
        }
    }
    return table[n];
}

int main()
{
//    vector<int> P = {1, 5, 8, 9};
    vector<int> P(1000);
    generate(P.begin(), P.end(), [] {return rand() % 10000 + 1;});
    sort(P.begin(), P.end());
    int n = P.size();

    auto start = high_resolution_clock::now();
//    cout << recursion(P, n) << endl;
    cout << tabular(P, n) << endl;
    auto end = high_resolution_clock::now();
    printf("elapsed %.4f seconds.", (end - start) * 1e-9);
}
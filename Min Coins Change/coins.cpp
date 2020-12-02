#include <iostream>
#include <climits>      // INT_MAX
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int mem[10001];

int recursion(int coins[], int n, int value)
{
    if (value == 0) return 0;

    if (mem[value] != INT_MAX - 1) return mem[value];

    int result = INT_MAX - 1;
    for (int i=0; i<n; i++)
    {
        if (coins[1] > value) continue;
        int remain = value - coins[i];
        result = min(result, 1 + recursion(coins, n, remain));
    }

    mem[value] = result;
    return mem[value];
}

int tabular(int coins[], int n, int value)
{
    int table[value + 1];
    fill_n(table, value + 1, INT_MAX -1);
    table[0] = 0;

    for (int v=1; v<=value; v++)
    {
        for (int i=0; i<n; i++)
        {
            if (coins[i] > v) continue;
            int remain = v - coins[i]; 
            table[v] = min(table[v], 1 + table[remain]);
        }
    }
    return table[value] != INT_MAX -1 ? table[value] : -1;
}

int main() 
{
    int coins[] = {1, 5, 6, 9};
    int value = 10000;
    int n = sizeof(coins) / sizeof(coins[0]);

    auto start = high_resolution_clock::now();
    //fill_n(mem, 10001, INT_MAX -1);
    //cout << recursion(coins, n, value) << endl;
    cout << tabular(coins, n, value) << endl;
    auto end = high_resolution_clock::now();
    printf("elapseed %.4f seconds.", (end- start) * 1e-9);
}
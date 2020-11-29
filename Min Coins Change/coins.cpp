#include <iostream>
#include <cstring>
#include <climits>
using namespace std;

int dp[100][100];

int minCoins(int coins[], int m, int n)
{
    if (n == 0) return 0;
    if (n < 0) return INT_MAX-1;
    if (m == 0 && n > 0) return INT_MAX-1;

    if (dp[m][n] != -1) return dp[m][n];

    int left = minCoins(coins, m-1, n); 
    int right = 1 + minCoins(coins, m, n - coins[m-1]);
    dp[m][n] = min(left, right);
    return dp[m][n];
}

int main() 
{
    memset(dp, -1, sizeof(dp));
    int coins[] = {9, 6, 5, 1};
    int n = 11;
    int m = sizeof(coins) / sizeof(coins[0]);

    cout << minCoins(coins, m, n) << endl;
}
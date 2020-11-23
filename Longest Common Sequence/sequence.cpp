#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int dp[100][100];

int longestCommonSequence(string X, string Y, int m, int n)
{
    if (m <= 0 || n <= 0) return 0;

    if (dp[m][n] != -1) return dp[m][n];

    if (X[m-1] == Y[n-1])
    {
        dp[m][n] = 1 + longestCommonSequence(X, Y, m-1, n-1); 
        return dp[m][n];
    } 

    int left = longestCommonSequence(X, Y, m, n-1);
    int right = longestCommonSequence(X, Y, m-1, n);
    dp[m][n] = max(left, right);
    return dp[m][n];
}

int main()
{
    memset(dp, -1, sizeof(dp));
    string X = "ABCBDAB";
    string Y = "BDCABA";
    int m = X.length();
    int n = Y.length();
    
    cout << longestCommonSequence(X, Y, m, n) << endl;
}


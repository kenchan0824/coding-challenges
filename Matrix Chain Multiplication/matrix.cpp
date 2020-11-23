#include <iostream>
#include <cstring>		// memset
#include <climits>		// INT_MAX
using namespace std;

int dp[100][100];

int matMulCost(int A[], int i, int j) 
{
	if (j <= i + 1) return 0;

	if (dp[i][j] != -1) return dp[i][j];

	int minCost = INT_MAX;
	for (int k=i+1; k<j; k++)
	{
		int cost = A[i] * A[k] * A[j];
		cost += matMulCost(A, i, k);
		cost += matMulCost(A, k, j);
		if (cost < minCost) minCost = cost;
	}
	dp[i][j] = minCost;
	return dp[i][j];
}

int main()
{
	memset(dp, -1, sizeof(dp));
	int A[] = {40, 20, 30, 10, 30};
	int j = sizeof(A) / sizeof(A[0]);
	cout << matMulCost(A, 0, j-1) << endl;
}
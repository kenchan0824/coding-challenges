#include <iostream>
#include <cstring>		// memset
#include <climits>		// INT_MAX
#include <vector>
#include <algorithm>	// generate_n
#include <random>		// rand
#include <chrono>
using namespace std;
using namespace std::chrono;

int mem[100][100];

int recursion(int const A[], int const i, int const j) 
{
	if (j <= i + 1) return 0;

	if (mem[i][j] != -1) return mem[i][j];

	int minCost = INT_MAX;
	for (int k=i+1; k<j; k++)
	{
		int cost = A[i] * A[k] * A[j];
		cost += recursion(A, i, k);
		cost += recursion(A, k, j);
		minCost = min(minCost, cost);
	}
	mem[i][j] = minCost;
	return mem[i][j];
}

int tabular(int const A[], int const n)
{
	vector<vector<int>> table(n, vector<int> (n, INT_MAX));
	
	for (int i=0; i<n-1; i++)
	{
		table[i][i+1] = 0;
	}

	for (int l=2; l<n; l++)
	{
		for (int i=0; i<n-l; i++)
		{
			int j = i + l;
			for (int k=i+1; k<j; k++)
			{
				int cost = A[i] * A[k] * A[j] + table[i][k] + table[k][j];
				table[i][j] = min(table[i][j], cost);
			}
		}
	}
	return table[0][n-1];
}

int main()
{

//	int A[] = {40, 20, 30, 10, 30};
//	int n = sizeof(A) / sizeof(A[0]);
	int n = 100;
	int A[n];
	generate_n(A, n, [] {return rand() % 100 + 1;});

	auto start = high_resolution_clock::now();
//	memset(mem, INT_MAX, sizeof(mem));
//	cout << recursion(A, 0, n-1) << endl;
	cout << tabular(A, n) << endl;
	auto end = high_resolution_clock::now();
	printf("elapsed %.4f seconds.", (end - start) * 1e-9);
}
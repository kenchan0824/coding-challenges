#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
using namespace std;
using namespace std::chrono;

int mem[1001][1001];

int recursion(string X, string Y, int m, int n)
{
    if (m <= 0 || n <= 0) return 0;

    if (mem[m][n] != -1) return mem[m][n];

    if (X[m-1] == Y[n-1])
    {
        mem[m][n] = 1 + recursion(X, Y, m-1, n-1); 
        return mem[m][n];
    } 

    int left = recursion(X, Y, m, n-1);
    int right = recursion(X, Y, m-1, n);
    mem[m][n] = max(left, right);
    return mem[m][n];
}

int tabular(string X, string Y)
{
    int m = X.size();
    int n = Y.size();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));

    for (int i=1; i<m+1; i++)
    {
        for (int j=1; j<n+1; j++)
        {
            if (X[i-1] == Y[j-1])
                L[i][j] = 1 + L[i-1][j-1];
            else
                L[i][j] = max(L[i][j-1], L[i-1][j]);
        }
    }
    return L[m][n];
}

int main()
{
    memset(mem, -1, sizeof(mem));
/*
    string X = "ABCBDAB";
    string Y = "BDCABA";
    int m = X.length();
    int n = Y.length();
*/
    int m = 1000;
    int n = 1000;
    string X;
    string Y;
    generate_n (back_inserter(X), m, [] {return static_cast<char> (rand() % 26 + 'A');});
    generate_n (back_inserter(Y), n, [] {return static_cast<char> (rand() % 26 + 'A');});

    auto start = high_resolution_clock::now();    
    //cout << recursion(X, Y, m, n) << endl;
    cout << tabular(X, Y) << endl;
    auto end = high_resolution_clock::now();
    printf("elapsed %.4f seconds.", (end - start) * 1e-9);
}


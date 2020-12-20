#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;

int solution(vector<int> A)
{
    int volume = 0;
    for(auto itr = A.begin()+1; itr != A.end()-1; itr++)
    {
        int left = *max_element(A.begin(), itr);
        int right = *max_element(itr+1, A.end());
        int level = min(left, right);
        volume += max(level - *itr, 0);
    }

    return volume;
}

int solution_fast(vector<int> A)
{
    int N = A.size();
    vector<int> right(N);
    right[N-1] = A[N-1];
    for(int i = N-2; i >= 0; i--)
    {
        right[i] = max(right[i + 1], A[i + 1]);
    }
    
    int volume = 0;
    int left = A[0];
    for(int i = 1; i < N-1; i++)
    {
        left = max(left, A[i-1]);
        int level = min(left, right[i]);
        volume += max(level - A[i], 0);
    }

    return volume;
}

int main()
{
    //vector<int> A = {0, 1, 4, 0, 0, 2, 0, 3, 1, 0};
    vector<int> A(1000000);
    generate(A.begin(), A.end(), [] {return rand() % 10;});
    auto begin = std::chrono::high_resolution_clock::now();
    
    cout << solution_fast(A) << endl;
    
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    printf("elapsed %.4f seconds.\n", elapsed.count() * 1e-9);
}
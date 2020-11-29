#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int solution(vector<int> &A)
{
    sort(A.begin(), A.end());
    
    auto front = A.end() - 1;
    auto back = A.begin();
    
    int min_sum = 2000000000;
    while (back != front)
    {
        min_sum = min(min_sum, abs(*front + *back));
        if (min_sum == 0) break;

        if (abs(*front) > abs(*back))
            front--;
        else
            back++;
    }

    min_sum = min(min_sum, abs(*front + *back));
    return min_sum;
}

int main()
{
    vector<int> A(100000);
    generate(A.begin(), A.end(), [] {return ((rand() * rand()) % 2000000000) - 1000000000;});
    
    auto start = high_resolution_clock::now();
    cout << solution(A) << endl;
    auto end = high_resolution_clock::now();
    printf("elapsed %.4f seconds", (end - start) * 1e-9);
}
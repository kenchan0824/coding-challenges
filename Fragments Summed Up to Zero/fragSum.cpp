#include <iostream>
#include <random>
#include <unordered_map>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int solution(int A[], int N)
{
    unordered_map<int, int> table;
    table[0] = 1;
    int count, psum = 0;
    for (int i=0; i<N; i++) {
        psum += A[i];
        count += table[psum];   // default to zero if psum not found
        table[psum] += 1;
    }
    return count;
}

int main()
{
    //int A[] = {2, -2, 3, 0, 4, -7};
    //int N = sizeof(A) / sizeof(A[0]);

    int N = 100000;
    int A[N];
    generate_n(A, N, []() {return rand() % 200 - 100;});

    auto start = high_resolution_clock::now();
    cout << solution(A, N) << endl;
    auto end = high_resolution_clock::now();
    printf("elapsed %.4f secound", (end - start) * 1e-9);

}

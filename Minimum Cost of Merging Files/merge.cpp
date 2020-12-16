#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <chrono>
using namespace std;
using namespace std::chrono;

int solution(vector<int> A)
{
    int cost = 0;
    while(A.size() > 1)
    {
        auto ptr = min_element(A.begin(), A.end());
        int min1 = *ptr;
        A.erase(ptr);

        ptr = min_element(A.begin(), A.end());
        int min2 = *ptr;
        A.erase(ptr);

        int merge = min1 + min2;
        A.push_back(merge);
        cost += merge;
    }
    return cost;
}

int solution_fast(vector<int> A)
{
    priority_queue
        <int, vector<int>, greater<int>> queue{A.begin(), A.end()};
    
    int cost = 0;
    while (queue.size() > 1)
    {
        int min1 = queue.top();
        queue.pop();
        int min2 = queue.top();
        queue.pop();
        int merge = min1 + min2;
        queue.push(merge);
        cost += merge;
    }
    return cost;
}

int main() 
{
    //vector<int> A = {14, 25, 5, 8};
    vector<int> A(100000);
    generate(A.begin(), A.end(), [] {return rand() % 100;});

    auto start = high_resolution_clock::now();

    cout << solution_fast(A) << endl;

    auto end = high_resolution_clock::now();
    auto elapsed = end - start;
    printf("elapsed %.4f seconds", elapsed * 1e-9);

    return 0;
}

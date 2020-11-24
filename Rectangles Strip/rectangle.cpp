#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> &A, vector<int> &B) 
{
    unordered_map<int, int> C;      // <length, counts>
    int N = A.size();
    for (int i=0; i<N; i++)
    {
        int a = A[i];
        if (C.find(a) == C.end()) 
            C[a] = 1;
        else 
            C[a] += 1;
        
        int b = B[i];
        if (b == a) continue;
        if (C.find(b) == C.end())
            C[b] = 1;
        else
            C[b] += 1;
    }

    int max = 0;
    for (auto itr = C.begin(); itr != C.end(); itr++) 
    { 
        if (itr->second > max) max = itr->second;
    } 

    return max;
}

int main()
{
    vector<int> A = {2, 10, 4, 1, 4};
    vector<int> B = {4, 1, 2, 2, 5};
    cout << solution(A, B) << endl;
}     
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binary_search(vector<int> const &L, int longest, int value)
{
    int start = 0;
    int end = longest - 1;

    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (L[mid] >= value)
            end = mid - 1;
        else
            start = mid + 1;        
    }
    return start;
} 

int solution(vector<int> const &A)
{
    int n = A.size();
    vector<int> L(n, -1);
    
    L[0] = A[0];
    int longest = 1;

    for (int i=1; i<n; i++)
    {
        int idx = binary_search(L, longest, A[i]);
        if (idx == longest) longest++;
        L[idx] = A[i];
    }

    return longest;
}

int main()
{
    vector<int> A = {0, 3, 4, 5, 2, 7, 3, 4, 5, 6};
    cout << solution(A) << endl;
}
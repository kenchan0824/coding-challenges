#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> const &A)
{
    int n = A.size();
    vector<int> L(n, -1);
    auto last = L.begin();
    for (int a : A)
    {
        auto itr = lower_bound(L.begin(), last, a);
        if (itr == last) last++;
        *itr = a;
    }
    return last - L.begin();
}

int main()
{
    vector<int> A = {0, 3, 4, 5, 2, 7, 3, 4, 5, 6};
    cout << solution(A) << endl;
}
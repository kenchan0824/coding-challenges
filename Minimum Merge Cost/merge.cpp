#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

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

int main() 
{
    vector<int> A = {14, 25, 5, 8};
    cout << solution(A) << endl;
    return 0;
}

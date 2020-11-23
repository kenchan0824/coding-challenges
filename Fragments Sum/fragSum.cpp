#include <iostream>
using namespace std;

int solution(int A[], int N)
{
    int count = 0;
    for (int i=0; i<N; i++)
    {
        int sum = 0;
        for (int j=i; j<N; j++)
        {
            sum += A[j];
            if (sum == 0) count++;
        }
    }
    return count;
}

int main()
{
    int A[] = {2, -2, 3, 0, 4, -7};
    int N = sizeof(A) / sizeof(A[0]);
    cout << solution(A, N) << endl;

}

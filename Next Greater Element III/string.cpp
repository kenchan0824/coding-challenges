#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int solution(int num) {
    string s = to_string(num);
    
    int i, j = i = s.size() - 1;
    while (i > 0 && s[i-1] >= s[i]) i--; 
    if (i == 0) return -1;
    
    while (j >= i && s[j] <= s[i-1]) j--;
    swap(s[i-1], s[j]);
    
    reverse(s.begin()+i, s.end());
    return stoll(s) <= INT32_MAX ? stoll(s) : -1;
}

int main() {
    int num = 1234765553;
    cout << solution(num) << endl;
    num = 765553;
    cout << solution(num) << endl;
    num = 1999999999;
    cout << solution(num) << endl;
}


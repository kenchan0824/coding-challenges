#include <iostream>
#include <string>
using namespace std;

string solution(string number) {
    string num, ans;
    for (char c : number) {
        if (c != ' ' &&  c != '-') num += c;
    }

    int i = 0, n = num.size(); 
    while (i < n) {
        int step = n-i == 4 || n-i == 2 ? 2 : 3;
        ans += num.substr(i, step) + "-";
        i += step;
    }
    ans.pop_back();
    return ans;
}

int main() {
    string number = "1-23-45 6";
    cout << solution(number) << endl;
    number = "123 4-567";
    cout << solution(number) << endl;
    number = "123 4-5678";
    cout << solution(number) << endl;
}
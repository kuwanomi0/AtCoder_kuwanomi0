#include <bits/stdc++.h>
using namespace std;

int A, B;

int main() {
    cin >> A >> B;
    int ans = A - B*2;
    if (ans < 0) ans = 0;
    cout << ans << endl;
}
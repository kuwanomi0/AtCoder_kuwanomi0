#include <bits/stdc++.h>
using namespace std;

const int COIN = 500;

int K, X;

int main() {
    cin >> K >> X;
    
    if (COIN * K >= X) puts("Yes");
    else puts("No");
}
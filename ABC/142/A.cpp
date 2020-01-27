#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
    scanf("%d", &N);
    double ans = (double)(N - N / 2) / (double)N;
    printf("%f\n", ans);
}
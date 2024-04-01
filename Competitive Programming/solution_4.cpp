#include<bits/stdc++.h>
using namespace std;

long long solve(long long a, long long b, long long m) {
    long long ans = 1;
    a = a % m;
    while (b > 0) {
        if (b % 2 == 1) {
            ans = (ans * a) % m;
        }
        b = b/2;
        a = (a * a) % m;
    }
    return ans;
}

int main() {
    long long a, b, m;
    cin >> a >> b >> m;
    long long ans = solve(a, b, m);
    cout << ans << "\n";
    return 0;
}

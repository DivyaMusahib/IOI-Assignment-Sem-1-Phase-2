#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin >> n;
    vector<int>arr;

    int isPrime[10001];
    for(int i=0; i<=10000; i++){
        isPrime[i]=1;
    }

    for(int j=2; j<=10000; j++){
        if(isPrime[j]==1){
            arr.push_back(j);
            for(int k= j*j; k<=10000; k=k+j){
                isPrime[k] =0;
            }
        }
    }

    cout << "First " << n << " alternate prime numbers will be ";

    for(int l=0; l<2*n; l=l+2){
        if(l!=2*(n-1)) cout << arr[l] << ", ";
        else cout << arr[l] << ".";
    }

    return 0;
}
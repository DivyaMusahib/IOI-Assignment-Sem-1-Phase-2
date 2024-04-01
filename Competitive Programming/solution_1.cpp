#include<bits/stdc++.h>
using namespace std;

int main(){

    int N;
    cin >> N;

    int arr[N], min, max, sum=0;
    float average=0, count=0;

    for(int i=0; i<N; i++){
        cin >> arr[i];
        if(i==0){
            min=arr[0], max=arr[0];
        }
        if(arr[i]<=min) min = arr[i];
        if(arr[i]>=max) max = arr[i];
        sum += arr[i];
        count++;
        average = sum/(float)count;

        cout << "min, max, sum and average after addition of "<< arr[i] << " is " << min << ", " << max << ", " << sum << ", " << average << ".\n";
    }
    return 0;
}
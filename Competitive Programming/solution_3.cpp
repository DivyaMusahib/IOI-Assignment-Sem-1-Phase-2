#include<bits/stdc++.h>
using namespace std;
int main(){
	int m, n;
    cout << "Enter size of 1st sorted array: ";
	cin >> m;
	int arr1[m];
	for (int i = 0; i < m; i++) {
		cin >> arr1[i];
	}

    cout << "Enter size of 2nd sorted array: ";
	cin >> n;
	int arr2[n];
	for (int i = 0; i < n; i++) {
		cin >> arr2[i];
	}
	int arr3[m + n];
	for (int i = 0, j = 0, k = 0; k < m + n; k++) {
		if (i < m && j < n) {
			if (arr1[i] <= arr2[j]) {
				arr3[k] = arr1[i++];
			} else {
				arr3[k] = arr2[j++];
			}
		} else if (i < m) {
			arr3[k] = arr1[i++];
		} else {
			arr3[k] = arr2[j++];
		}
	}
	for (int z = 0; z < m + n; z++) {
		cout << arr3[z] << " ";
	}
}
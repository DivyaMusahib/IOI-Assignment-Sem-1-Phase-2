#include <iostream>
#include <vector>

using namespace std;

int lower_bound(const vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;
    int result = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] >= x) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return result;
}

int upper_bound(const vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;
    int result = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] > x) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return result;
}

bool is_present(const vector<int>& arr, int x) {
    int index = lower_bound(arr, x);
    return (index != -1 && arr[index] == x);
}

int main() {
    int n;
    cout << "Enter size of the sorted array: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter sorted array.";
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    int x;
    cout << "Enter x: ";
    cin >> x;

    cout << "Lower Bound of x: " << lower_bound(arr,x) << endl;
    cout << "Upper Bound of 10: " << upper_bound(arr, x) << endl;
    cout << "Is x present? " << is_present(arr, x) << endl;

    return 0;
}

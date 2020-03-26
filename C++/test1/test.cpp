#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#pragma warning(disable : 4996)
using namespace std;

int num, m;
int val[100005];
int findmax(int *lst, double a, int left, int right)
{
    if (right - left <= 1)
        return left;
    if (a <= lst[left])
        return 0;
    if (a > lst[right - 1])
        return right;
    long mid = long((left + right) / 2);
    if (lst[mid] >= a && lst[mid - 1] < a)
        return mid;
    if (lst[mid] >= a)
        return findmax(lst, a, left, mid + 1);
    else
        return findmax(lst, a, mid + 1, right);
}
bool check(int mid)
{
    int i, sum = 0;

    for (i = 0; i < num; i++)
    {
        sum += (findmax(val, val[i] + mid + 1, 0, num) - (i)-1);
    }
    if (sum >= m)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{

    int a[] = {1, 2, 3, 4};
    int i = 0;
    cout << a[i++] << i;
    return 0;
}
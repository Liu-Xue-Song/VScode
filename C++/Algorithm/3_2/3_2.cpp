#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

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
        sum += (lower_bound(val + i, val + num, val[i] + mid + 1) - (val + i) - 1);
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
    //freopen("i.txt","r",stdin);
    //freopen("o.txt","w",stdout);

    int i, left, right, mid;
    while (scanf("%d", &num) != EOF)
    {
        for (i = 0; i < num; i++)
        {
            scanf("%d", &val[i]);
        }
        m = (num * (num - 1) / 2 + 1) / 2;
        sort(val, val + num);

        left = 0;
        right = val[num - 1] - val[0];

        while (right - left > 1)
        {
            mid = (left + right) / 2;

            if (check(mid))
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }
        cout << right << endl;
    }
    return 0;
}
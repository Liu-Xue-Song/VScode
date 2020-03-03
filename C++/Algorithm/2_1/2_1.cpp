#include <iostream>
using namespace std;

int isv(int a[], int x, int k)
{
    int y = 1;
    for (int i = 0; i < k; i++)
    {
        if (x == a[i] || abs(x - a[i]) == abs(k - i))
        {
            y = 0;
            break;
        }
    }
    return y;
}

void queen(int a[], int k, int n, int *count)
{
    for (int i = 0; i < n; i++)
    {
        if (isv(a, i, k) == 1)
        {
            a[k] = i;
            if (k == n - 1)
            {
                count[0]++;
            }
            else
            {
                queen(a, k + 1, n, count);
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;
    int count[1];
    count[0] = 0;
    int *a = new int[n];
    queen(a, 0, n, count);
    cout << count[0] << endl;
    return 0;
}

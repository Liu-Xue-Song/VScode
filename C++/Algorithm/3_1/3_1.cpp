#include <iostream>
using namespace std;
int search(int *a, int k, int end, int n)
{
    if (end - k < 2)
        return a[k];
    // else
    //     while
    else
    {
        int s = k;
        int e = end - 1;
        int temp = a[k];
        while (s < e)
        {
            while (a[e] >= temp && s < e)
                e--;
            if (s < e)
            {
                a[s] = a[e];
                s++;
            }
            while (a[s] < temp && s < e)
                s++;
            if (s < e)
            {
                a[e] = a[s];
                e--;
            }
        }
        e = s;
        a[e] = temp;
        if (e == int((n - 1) / 2))
            return a[e];
        else if (e < int((n - 1) / 2))
            return search(a, e + 1, end, n);
        else
            return search(a, k, e, n);
    }
}

int main()
{
    int n;
    cin >> n;
    int *a = new int[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    double r = search(a, 0, n, n);
    printf("%.6f", r);
}
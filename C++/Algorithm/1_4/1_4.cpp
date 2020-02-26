#include <iostream>
using namespace std;
//int count = 0;
void merge(long p[], long l, long r, long *t, long *count)
{
    long mid = (l + r) / 2;
    long i = l;
    long j = mid + 1;
    long k = l;
    while (i <= mid && j <= r)
    {
        if (p[i] <= p[j])
            t[k++] = p[i++];
        else
        {
            t[k++] = p[j++];
            *count += mid - i + 1;
        }
    }
    while (i <= mid)
        t[k++] = p[i++];
    while (j <= r)
        t[k++] = p[j++];
    for (long i = l; i <= r; i++)
        p[i] = t[i];
}
void sort(long *p, long l, long r, long *t, long *count)
{
    if (l < r)
    {
        long mid = (l + r) / 2;
        sort(p, l, mid, t, count);
        sort(p, mid + 1, r, t, count);
        merge(p, l, r, t, count); 
    }
}
int main()
{
    long n;
    cin >> n;
    long *p = new long[n];
    long *t = new long[n];
    long count = 0;
    for (long i = 0; i < n; i++)
        cin >> p[i];
    sort(p, 0, n - 1, t, &count);
    cout << count << endl;
}
#include <iostream>
using namespace std;
void move(int s, int e, int a)
{
    if (a == 1)
        cout << char(64 + s) << "-" << char(64 + e) << endl;
    else
    {
        move(s, 6 - s - e, a - 1);
        cout << char(64 + s) << "-" << char(64 + e) << endl;
        move(6 - s - e, e, a - 1);
    }
}
int main()
{
    int a;
    while (cin >> a)
    {
        move(1, 3, a);
    }
    return 0;
}
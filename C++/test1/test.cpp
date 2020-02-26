#include <iostream>
using namespace std;
int main()
{
    int a = 1;
    int b = 2;
    int c = a + b;
    int d = c + b;
    if (a == b)
        b = 1;
    a = 1;
    cout << d << endl;
    cout << "hello world" << endl;
    return 0;
} //1223
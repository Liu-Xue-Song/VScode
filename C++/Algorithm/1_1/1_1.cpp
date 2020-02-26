#include<iostream>
using namespace std;
int main()
{
    double p = 0;
    double n = 0;
    for (int i = 0; i < 10;i++)
    {
        double x;
        cin >> x;
        if(x>0)
            p += x;
        else
        {
            n+= x;
        }
    }
    printf_s("%.2f", p);
    printf_s(",");
    printf_s("%.2f", n);
    printf_s(",");
    printf_s("%.2f", n + p);
}
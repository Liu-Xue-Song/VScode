#include <algorithm>
#include <iostream>
using namespace std;
void change(int *, int *);
int pivot(int *, int, int);
int pivotRow(int *, int, int, int);
void mid5(int *lst, int s)
{
    if (lst[0 + s] > lst[1 + s])
        change(lst + s, lst + s + 1);
    if (lst[2 + s] > lst[3 + s])
        change(lst + s + 2, lst + s + 3);
    if (lst[1 + s] > lst[3 + s])
    {
        change(lst + s + 1, lst + s + 4);
        if (lst[0 + s] > lst[1 + s])
            change(lst + s, lst + s + 1);
    }
    else
    {
        change(lst + s + 4, lst + s + 4);
        if (lst[2 + s] > lst[3 + s])
            change(lst + s + 2, lst + s + 3);
    }
    if (lst[1 + s] > lst[3 + s])
    {
        change(lst + s, lst + s + 2);
        change(lst + s + 1, lst + s + 3);
    }
    if (lst[1 + s] > lst[2 + s])
        change(lst + s + 2, lst + s + 1);
}

void change(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int pivot(int *lst, int left, int right)
{
    if (right - left <= 5)
    {
        sort(lst + left, lst + right);
        return lst[int((left + right) / 2)];
    }
    else
    {
        int num = right - left;
        int *more = new int[num];
        int colNum = num / 5;
        int **table = new int *[5];
        int mk = 0;
        for (mk; mk + 5 * colNum + left < right; mk++)
        {
            more[mk] = lst[5 * colNum + mk + left];
        }
        for (int i = 0; i < 5; i++)
        {
            table[i] = new int[colNum];
        }
        for (int i = 0; i < colNum; i++)
        {
            mid5(lst, i * 5 + left);
            for (int j = 0; j < 5; j++)
            {
                table[j][i] = lst[5 * i + j + left];
            }
        }
        int m = pivotRow(table[2], colNum, 0, colNum);
        int s = 0; //
        int e = num - 1;
        //int mk = 0;
        for (int i = 0; i < colNum; i++)
        {
            int j = 0;
            if (table[2][i] < m)
            {
                for (j; j < 3; j++)
                    lst[left + s++] = table[j][i];
                for (j; j < 5; j++)
                    more[mk++] = table[j][i];
            }
            else if (table[2][i] > m)
            {
                for (j; j < 2; j++)
                    more[mk++] = table[j][i];
                for (j; j < 5; j++)
                    lst[left + e--] = table[j][i];
            }
            else
            {
                for (j; j < 2; j++)
                    lst[left + e++] = table[j][i];
                for (j + 1; j < 5; j++)
                    lst[left + e--] = table[j][i];
            }
        }
        for (int i = 0; i < mk; i++)
        {
            if (more[i] < m)
                lst[left + s++] = more[i];
            else
                lst[left + e--] = more[i];
        }
        lst[s + left] = m;
        for (int i = 0; i < 5; i++)
            delete[] table[i];
        delete[] table;
        table = NULL;
        delete[] more;
        more = NULL;
        return s + left;
    }
}

int pivotRow(int *lst, int n, int left, int right)
{
    if (right - left <= 5)
    {
        sort(lst + left, lst + right);
        return lst[(left + right) / 2];
    }
    else
    {
        int num = right - num;
        int colNum = num / 5;
        int *table = new int[colNum];
        int c = left;
        for (int i = 0; i < colNum; i++)
        {
            mid5(lst, c);
            table[i] = lst[c + 2];
            c += 5;
        }
        return pivotRow(table, colNum, 0, colNum);
    }
}
int findk(int *lst, int k, int left, int right)
{
    if (right - left <= 5)
    {
        sort(lst + left, lst + right);
        return lst[k - 1];
    }
    else
    {
        int s = pivot(lst, left, right);
        if (s == k - 1)
            return lst[s];
        else if (s > k - 1)
            return findk(lst, k, left, s);
        else
            return findk(lst, k, s + 1, right);
    }
}

int main()
{
    int n;
    cin >> n;
    int k;
    cin >> k;
    int *lst = new int[n];
    for (int i = 0; i < n; i++)
        cin >> lst[i];
    int y = findk(lst, k, 0, n);
    cout << y;
    delete[] lst;
    lst = NULL;
    return 0;
}
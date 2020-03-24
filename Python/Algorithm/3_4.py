#Heap sort
#all start from 1
import math

# def fixHeap(lst, root, k, n):
#     left = 2 * root
#     right = 2 * root + 1
#     if left > n:
#         lst[root] = k
#     else:
#         if left == n:
#             larger = left
#         elif lst[left] > lst[right]:
#             larger = left
#         else:
#             larger = right
#         if k >= lst[larger]:
#             lst[root] = k
#         else:
#             lst[root] = lst[larger]
#             fixHeap(lst, larger, k, n)


def heapSort(lst, n):
    h = 1 + math.floor(math.log(n, 2))
    constructHeap(lst, 1, h)
    for i in range(n, 1, -1):
        Max = lst[1]
        K = lst[i]
        h = math.floor(math.log(i - 1, 2)) + 1
        lst[:i] = fixHeapDC((lst[:i]), 1, K, h)
        lst[i] = Max


def constructHeap(lst, root, h):
    if 2 * root > len(lst):
        return
    else:
        constructHeap(lst, 2 * root, h - 1)
        constructHeap(lst, 2 * root + 1, h - 1)
        k = lst[root]
        hRoot = 1 + math.floor(math.log(root, 2))
        fixHeapDC(lst, root, k, h)
    return


def bubbleUpHeap(lst, root, k, vacant):
    if vacant == root:
        lst[vacant] = k
    else:
        parent = int(vacant / 2)
        if k < lst[parent]:
            lst[vacant] = k
        else:
            lst[vacant] = lst[parent]
            bubbleUpHeap(lst, root, k, parent)


def promote(lst, hStop, vacant, h):  #search down find middle of root and leaf
    if h <= hStop or 2 * vacant > len(lst) - 1:
        vStop = vacant
    elif 2 * vacant + 1 > len(lst) - 1:
        lst[vacant] = lst[2 * vacant]
        vStop = promote(lst, hStop, 2 * vacant, h - 1)
    elif lst[2 * vacant] <= lst[2 * vacant + 1]:
        lst[vacant] = lst[2 * vacant + 1]
        vStop = promote(lst, hStop, 2 * vacant + 1, h - 1)
    else:
        lst[vacant] = lst[2 * vacant]
        vStop = promote(lst, hStop, 2 * vacant, h - 1)
    return vStop


def fixHeapDC(lst, vacant, k, h):
    if h <= 1:
        lst[vacant] = k
    else:
        hStop = int(h / 2)
        vStop = promote(lst, hStop, vacant, h)
        vParent = int(vStop / 2)
        if lst[vParent] <= k:
            lst[vStop] = lst[vParent]
            bubbleUpHeap(lst, vacant, k, vParent)
        else:
            fixHeapDC(lst, vStop, k, hStop)
    return lst


n = eval(input())
ls = [eval(x) for x in input().split()]
lst = [0]
lst.extend(ls)
heapSort(lst, n)
# if lst[1] > lst[2]:
#     lst[1], lst[2] = lst[2], lst[1]
for i in lst[1:]:
    print(i, end=' ')

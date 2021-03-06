"""
小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）

输入描述：
输入第一行将包含一个数字n，代表楼的栋数，接下来的一行将包含n个数字wi(1<=i<=n)
代表每一栋楼的高度。
1<=n<=100000;1<=wi<=100000;

输出描述：
输出一行，包含空格分割的n个数字vi，分别代表小Q在第i栋楼时能看到的楼的数量。

输入例子：
6
5 3 8 3 2 5
1
2

输出例子：
3 3 5 4 4 4

例子说明：
当小Q处于位置3时，他可以向前看到位置2,1处的楼，向后看到位置4,6处的楼，加上第3栋
楼，共可看到5栋楼。当小Q处于位置4时，他可以向前看到位置3处的楼，向后看到位置5,6
处的楼，加上第4栋楼，共可看到4栋楼。
"""

#暴力求解，通过率40%
def shopping(n, w):
    left = [0] * n
    right = [0] * n
    for i in range(n - 1):
        r = 1
        temp = w[i + 1]
        for j in range(i + 2, n):
            if temp < w[j]:
                temp = w[j]
                r += 1   
        right[i] = r
    for i in range(n - 1, 0, -1):
        l = 1
        temp = w[i - 1]
        for j in range(i - 2, -1, -1):
            if temp < w[j]:
                temp = w[j]
                l += 1
        left[i] = l
    for i in range(n):
        count[i] = left[i] + right[i] + 1 

if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * n
    shopping(n, a)
    print(" ".join(str(s) for s in count))

#通过率100%
def building(n, w):
    right = []
    left = []
    r = [0] * n
    l = [0] * n
    count = [1] * n
    for i in range(n):
        r[i] = len(right)
        if i == 0 or w[i] < right[-1:].pop():
            right.append(w[i])
        else:
            while len(right) != 0 and w[i] >= right[-1:].pop():
                right.pop()
            right.append(w[i])
    for j in range(n - 1, -1, -1):
        l[j] = len(left)
        if j == n - 1 or w[j] < left[-1:].pop():
            left.append(w[j])
        else:
            while len(left) != 0 and w[j] >= left[-1:].pop():
                left.pop()
            left.append(w[j])
    for k in range(n):
        count[k] = r[k] + l[k]
    return ' '.join(str(s) for s in count)
    

if __name__=='__main__':
#     n = 6
#     w = [5,3,8,3,2,5]
    n = int(input())
    w = list(map(int, input().split()))
    print(building(n, w))

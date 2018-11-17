def insert_sort(alist):
    """
    i从1到列表的长度-1
    j=i
    whlie循环，条件小于1终止
    第一次i=1
    判断alist[j]<alist[j-1]，也就是 alist[1]<alist[0]?
    小于就alist[1]和alist[0]互换
    j=j-1，j变成0，退出循环
    """
    """
    i从1到列表的长度-1
    j=i
    whlie循环，条件小于1终止
    第一次i=2
    判断alist[j]<alist[j-1]，也就是 alist[2]<alist[1]?
    小于就alist[2]和alist[1]互换
    j=j-1，j变成1，继续判断
    判断alist[j]<alist[j-1]，也就是 alist[1]<alist[0]?
    小于就alist[1]和alist[0]互换
    j=j-1，j变成0，退出循环
    以此类推
    """
    n=len(alist)
    for i in range(1,n):
        j=i
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
                j -= 1
            else:
                break

if __name__=="__main__":
    alist=[54,26,93,17,77,31,44,55,20]
    print(alist)
    insert_sort(alist)
    print(alist)
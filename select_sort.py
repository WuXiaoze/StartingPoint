def select_sort(alist):
    """
    for循环，i从0到列表的长度-1
    先给min_index一个默认值
    j第一次走从i+1开始到n，也就是n-1，range最后一个不计入
    假设列表长度是9，j就是1到8
    用alist[min_index]跟alist[j]比较，
    前者大于后者，就把坐标赋给min_index
    记录下最小值的坐标位置
    退出循环后把最小值放到i所指的索引
    第一次循环i是0
    这样就把最小的值放到了最前面
    alist[17,26,93,54,77,31,44,55,20]
    也可以反过来去最大值，从大到小排序
    """

    """
    for循环，第二次i从1到列表的长度-1
    先给min_index一个默认值
    j从i+1开始到n，也就是n-1，range最后一个不计入
    假设列表长度是9，第二次j就是2到8
    用alist[min_index]跟alist[j]比较，
    前者大于后者，就把坐标赋给min_index
    记录下最小值的坐标位置
    退出循环后把最小值放到i所指的索引
    第二次循环i是1
    这样就把这次找到的最小值放到了第二位
    alist[17,20,93,54,77,31,44,55,26]

    以此类推
    """
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]



if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    select_sort(alist)
    print(alist)

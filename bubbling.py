def bubble_sort(alist):
    '''
    第一次走内层的for循环
    外层i从0到列表的长度-1
    内层j从0到n-1-j，此时n-1就是整个列表的长度，
    再减i，因为i第一次走是0，所以会遍历整个列表
    依次拿alist[0]和alist[1]，步长值偏差1对比，
    前者比后者大就互换位置
    走完一圈alist变成[26,54,17,77,31,44,55,20,93]
    最大的数字已经移到了列表的最后面
    '''

    '''
    第二次走内层的for循环
    外层i从1到列表的长度-1
    内层j从0到n-1-j，此时n-1就是整个列表的长度，
    再减i，因为i第二次走是1，所以会遍历整个列表到倒数第二个元素
    因为最后一个已经是最大值
    依次拿alist[0]和alist[1]，步长值偏差1对比，
    前者比后者大就互换位置
    走完一圈alist变成[26,17,54,31,44,55,20,77,93]
    第二大的数字已经移到了列表的倒数第二位
    '''

    '''
    以此类推，到整个内层循环走完，count计数为0的时候，not取反，if True return退出
    '''
    n = len(alist)
    for i in range(n-1):
        count=0
        for j in range(0,n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                count += 1
        #count等于0表示没有成立的，就退出
        if not count:
            return

if __name__ == "__main__":
    list=[54,26,93,17,77,31,44,55,20]
    print(list)
    bubble_sort(list)
    print(list)
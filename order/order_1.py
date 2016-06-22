a=[31,41,59,26,41,58,38,18]


# 1,插入排序-增量方法

def insert_sort(array):
    for j in range(1,len(array)):
        latter=a[j]
        i=j-1
        while i>=0 and a[i]<latter:  # 决定是降序还是升序
            a[i+1]=a[i]
            i=i-1
            a[i+1]=latter

print(insert_sort(a))


# 循环不变性的三个性质:初始化/保持/终止
# 分治方法-将原始问题划分成n个小规模,且结构与原问题相似的自问题-递归

# 2,选择排序


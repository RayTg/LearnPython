# 循环不变性的三个性质:初始化/保持/终止
# 分治方法-将原始问题划分成n个小规模,且结构与原问题相似的自问题-递归
# 排序算法一般不超过下面这11种情况
#1 Simple sorts
#   1.1 Insertion sort(插入排序)
#   1.2 Selection sort(选择排序)
#
#2 Efficient sorts
#   2.1 Merge sort (归并排序)
#   2.2 Heapsort  (堆排序)
#   2.3 Quicksort (快速排序)
#
#3 Bubble sort and variants
#  3.1 Bubble sort (冒泡排序)
#  3.2 Shell sort (希尔排序)
#  3.3 Comb sort (梳排序)
#
#4 Distribution sort
#  4.1 Counting sort(计数排序)
#  4.2 Bucket sort(桶排序)
#  4.3 Radix sort(基数排序)
#########################################################################################

if __name__ == '__main__':
    A = [4, 9, 1, 13, 34, 26, 10, 7, 4]

# 1.1,插入排序
# 算法流程：遍历把每个元素，按照这个元素前面的数组中，根据大小决定的位置，插入该元素
# 最好：已经排好顺序的集合，这样只需要线性时间即遍历一次集合，每次只需要比较当前元素与前一个元素的大小问题，时间复杂度O(n)
# 最坏：即刚好与所要的顺序相反，时间复杂度为O(n^2)
# 平均：时间复杂度也是O(n^2)

def insert_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:  # 升序
            # print(array)
            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp
            j -= 1
    return array
# insert_sort(A)



# 1.2, 选择排序
# 算法流程：将数组分为两部分，一部分是已经排好顺序的，另一部分是未排序的。每次找数组后半部分中最小的一个元素排到前面的序列
# 选择排序最坏，最好，平均情况都是O(n^2).

def select_sort(array):
    n=len(array)
    for i in range(n):
        iMin = i
        for j in range(i+1, n):
            if array[iMin] > array[j]:    #不断替换最小的索引
                iMin = j

            tmp = array[i]
            array[i] = array[iMin]
            array[iMin] = tmp

    return array


#select_sort(A)


# 插入排序与选择排序的区别

# 插入排序类似于选择排序，不同之处是插入排序是一个元素一个元素地往有序序列中插入，
# 而选择排序则是在无序序列中选择最大(最小)元素放入有序队列末尾。
# 一个主要操作有序队列，一个则是无序队列。这样就导致选择排序每次都要遍历一次无序队列，
# 而插入排序则不需要遍历整个有序队列，只需要遍历到该元素应有的位置即可，这样就使得基本有序的队列的复杂度为O(n)
# 但同时这会导致插入排序用到更多的写操作，因为内部循环时他对数组进行大量的移位操作，
# 大家知道移位操作对于数组是非常低效率的。而选择排序因为每次添加元素都是添加在末尾，所以不需要移位操作。
#########################################################################################



# 2.1, 归并排序
# 算法：是一种基于“分治”策略的一种算法。
# 归并排序算法是典型的分治算法，对于规模较大的问题，可以分解成若干容易求解的简单的问题，最后把解合并构成初始问题的解

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])    #先拆分，直到最小单元
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if len(left) > 0:
        result.extend(merge_sort(left)) #剩下的列表全部添加到result中
    else:
        result.extend(merge_sort(right))
    return result

#print(merge_sort(A))

# 2.2, 堆排序
# 算法：是数据结构-堆，堆排序是选择排序种类的一部分。它的提升是用到了对数时间优先队列（即堆）而不是线性时间搜索。
# 堆排序是一种 in-place algorithm，但不是稳定的排序。
# 算法流程：
# 建立一个最大或最小堆
# 用根元素与最后一个元素交换位置，将根元素从堆中移除，堆大小减小1。
# 修复堆，回到上一步，直到堆中不剩元素。

#def heap_sort(array):


# 2.3, 快速排序




#  3.1 冒泡排序
# 冒泡排序效率非常低，效率还不如插入排序。数据量大时效率低，对于顺序颠倒的序列效率最低。
# 算法流程：简单概括就是每次找到序列中最大或最小的元素排到最后面去，循环知道每个元素都处于正确位置。

def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n-1):
            if array[j] > array[j+1]:
                tmp = array[j+1]
                array[j+1] = array[j]
                array[j] = tmp

    return  array

#print(bubble_sort(A))

#  3.2 希尔排序
# 希尔排序是in-place算法，但不是稳定的，其实质就是分组插入排序
# 算法流程：
# 先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）
# 分别进行直接插入排序，
# 然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
# 因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。


def shell_sort(array):
    gap = len(array)/2
    while gap > 0:




        gap/=2





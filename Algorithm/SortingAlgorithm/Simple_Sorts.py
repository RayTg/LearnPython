# 循环不变性的三个性质:初始化/保持/终止
# 分治方法-将原始问题划分成n个小规模,且结构与原问题相似的自问题-递归

# 1,插入排序
# 对于少量数据效率高
# 最好：已经排好顺序的集合，这样只需要线性时间即遍历一次集合，每次只需要比较当前元素与前一个元素的大小问题，时间复杂度O(n)
# 最坏：即刚好与所要的顺序相反，时间复杂度为O(n^2)
# 平均：时间复杂度也是O(n^2)

A = [21, 12, 6, 34, 29, 15]

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
# print(insert_sort(A))



# 2, 选择排序

def select_sort(array):
    for i in range(1,len(array)):
        j=i

























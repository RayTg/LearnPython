a=[31,41,59,26,41,58]
print(a)


#插入算法-增量方法

for j in range(1,len(a)):
    latter=a[j]
    i=j-1
    while i>=0 and a[i]<latter:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=latter

print(a)


# 循环不变性的三个性质:初始化/保持/终止

# 分治方法-将原始问题划分成n个小规模,且结构与原问题相似的自问题-递归


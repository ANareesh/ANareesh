########pandas
import pandas as pd


# print(pd.__version__)
# a=['a','b','c']
# b=['10','20','30']
#
# c=pd.Series(data=a)
# print(c)
# index

# a=['a','b','c']
# b=['10','20','30']
#
# c=pd.Series(data=b,index=a)
# print(c)

##dic

#
# d={"a":"1","b":"2","c":"3"}
# q=pd.Series(data=d)
# print(q)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# d={"a":"1","b":"2","c":"3"}
# q=pd.Series(data=d,index=["a","b"])
# print(q)


########DATAFRAME
# list
# l=["1","2","3","4","5","6"]
# q=pd.DataFrame(l,index=["a","b","c","d","e","f"])
# print(q)

# dict
# d={"a":["1","2","3","4","5"],"b":["a","b","c","d","e"]}
# q=pd.DataFrame(d)
# print(q)


# Dealing with Rows and Columns
# Column Selection
# Define a dictionary containing employee
# data = {'Name'          : ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age'           : [27, 24, 22, 32],
#         'Address'       : ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification' : ['Msc', 'MA', 'MCA', 'Phd']}
# q=pd.DataFrame(data)
# print(q)
# # print(q[['Age', 'Qualification']])

# row selection
#
# q=pd.read_csv("C:\\Users\\DELL\\PycharmProjects\\pandas\\pandas.csv")
#
# # first=q.loc["jai"]
# # second=q.loc["anuj"]
# # print(first)
# # print(second)
# print(q)
# swapping two numbers
# 1
# x=10
# y=20
# temp = x
# x=y
# y=temp
# print(x)
# print(y)

# 2 Without Using Temporary Variable
# x=10
# y=20
#
# x,y = y,x
# print(x)
# print(y)

# reverse integer

# n = int(input("please give a number : "))
# reverse = 0
# while n!=0:
#     reverse = reverse*10 + n%10
#     n = (n//10)
# print(reverse)




# 4


# Binary Search in python

#
# def binarySearch(array, x, low, high):
#     while low <= high:
#         mid = low + (high - low) // 2
#         if array[mid] == x:
#             return mid
#         elif array[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x, 0, len(array) - 1)
# if result != -1:
#     print(result)
# else:
#     print("Not found")





##fibonacci upto n numbers

# num=10
# n1,n2=0,1
# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end="")
##factorial recursion

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))
# print(factorial(3))



##poly

# n=121
# p=n
# res=0
# while n!=0:
#     r=n%10
#     res = res*10+r
#     n=n//10
# if p==res:
#     print("poly")
# else:
#     print("not poly")




#2me



hellllllllll
asdfgddfghj
dfgfhjkhgfds
jicicekisqlm
kiwetry

wertu
properqqw
qer
wx
nfh
hsk
qwerty



hiiiiiiiiiiiiiiiiiiiii


assert
wer
errnoc
bv
vb
types
bn
from















# n=121
# p=n
# res=0
# n=121
# p=n
# res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0# n=121
# # p=n
# # res=0


# # res=0# n=121
# # p=n
# # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0# # res=0# n=121
# # # p=n
# # # res=0
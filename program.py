from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# ### 1 flatlist
# # # 2 non repeted elements
# # ## 3 binary search
# # ## 4 bubble_sort
# # ## 5 reverse a integer
# # ## # 6 swapping two numbers without using 3rd number
# # ## 7 sum_split_list
# # ##  8 dict key value number
# # ### 9  how many combination  in a list
# # ## 10 first n numbers fibinoc series
# # #### 11 factorial of a number
# # ##  12 find first n prime numbers
# # ## 13 find key index position key value
# 13.1 to get items in a dictionary
# 13.2 to get only keys in a dictionary
## 13.3 to get only values in a dictionary
# #### 14 json to dict
# ###  15  is_perfect_number
# # ####  16 string values repeting
# ### 17 counting list values into single element
# # ### 18  second max value in a list
# ### 19 how to find 3rd highest number
# # ##### 20  remove duplicate in a neasted list values in a list
# #### 21 ip="aaabbbaabbcc" op= 3a3b2a2b2c
# ###  22 all zeros at end op=[1, 2, 3, 4, 5, 0, 0]
# ### 23 amstrong  number
# ### 24 list element in assending order
# #### 25 removing duplicates from list
# ### 26 ip=[[1,2,3],[4,5,6],[7,8,9]] op= [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# ### 27 find all occurrence element in a list
# ### 28 occurence element in a list
# ### 29 sort a dictionary key
# #### 30 prime numbers
# ## 31 swap key to values and values to key
# ### 32  reversa a list values l=["1","2","3"]  ['3', '2', '1']
# ### 33 first 10 first 10 fibonnaci series
# ###  34 only keys reverse in a dict
# ### 35 target number
# ####  36 if l=[9,9,9] op = [1, 0, 0, 0]
#### 37 getting multiple datatypes values in a list
####  38 l= ['hello', 'world', 'python']    Output: ['HELLO', 'WORLD', 'PYTHON']
#### 39 lambda function example program filter map reduce function
####40 l=[1,2,3,4] op={1: 2, 2: 4, 3: 6, 4: 8}
#### 41 dict sort values
### 41.1 sort key dictionary
### 42 l=[1,2,3,4,"are","hi",5,{"hi","fg"}] op=[1,2,3,4,"ARE","HI",5,{"HI","FG"}]
##### 43 in a string of list  or set i want to get list or set  out of string
###44 i want to separate list values and set values in a string
##### 45 Fibonacci byusing init,iter,next methods
## 46 find the maximum length of consecutive zero's in a binary string
### 47 If you want to see only the migrations that have not been applied yet, run

# 48 str1 = "abcde"# if n=5 than output will be "abcde"# if n=3 than "abc"# if n=7 than "abcdeab"if n=11 than "abcdeabcdea"# if n=15 than "abcdeabcdeabcde"
###49 input "my name is nareesh"  output=NAREESH IS NAME MY
###  50 oops

#
# ###1 flatlist
# # l = [[1, 2, 3], [4, 5], [54], [], [6, [7, 8]], 9]
# # l1=[]
# # l2=[l]
# # while l2:
# #     c = l2.pop()
# #     for i in c:
# #         if isinstance(i,list):
# #             l2.append(i)
# #         else:
# #             l1.append(i)
# #
# # print(l1)
# #
# # # 2 non repeted elements
# #
# # def elements(lst):
# #     c = {}
# #     for i in lst:
# #         if i in c:
# #             c[i] += 1
# #         else:
# #             c[i] = 1
# #     l1 = []
# #     for j, count in c.items():
# #         if count == 1:
# #             l1.append(j)
# #     return l1
# # print(elements([3,2,3,4,5,2,5,6,7,]))
# #
#
#
#
#
# l=[9, 6, 7, 8,1,2,3,4,2,3,1,3]
# c={}
# l1=[]
# for i in l:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)
# for j,count in c.items():
#     if count==1:
#         l1.append(j)
# print(l1)
# #
# # ## 3 binary search
# #
# #
# # def binary(a, b):
# #     start = 0
# #     end = len(a) - 1
# #     while (start <= end):
# #         mid = (start + end) // 2
# #         if (a[mid] > b):
# #             end = mid - 1
# #         elif (a[mid] < b):
# #             start = mid + 1
# #         else:
# #             return mid
# #
# #
# # print(binary([1, 2, 3, 4, 5, 6], 6))
# #
# #
# # ## 4 bubble_sort
# #
# #
# # def bubble_sort(list1):
# #     for i in range(0, len(list1) - 1):
# #         for j in range(len(list1) - 1):
# #             if list1[j] > list1[j + 1]:
# #                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
# #     return list1
# #
# #
# # list1 = [5, 3, 8, 6, 7, 2]
# # print(bubble_sort(list1))
# #
# # l = [5, 3, 8, 6, 7, 2]
# # for i in range(len(l)-1):
# #     for j in range(i+1,len(l)):
# #         if l[j]<l[i]:
# #             l[i],l[j]=l[j],l[i]
# # print(l)
# #
# #
# # ## 5 reverse a integer
# #
# # num = 12345
# # rev = 0
# #
# # while num > 0:
# #     digit = num % 10
# #     rev = rev * 10 + digit
# #     num = num // 10
# #
# # print(rev)
# #
# # ## # 6 swapping two numbers without using 3rd number
# #
# # a = 10
# # b = 20
# #
# #
# # a = a ^ b
# # b = a ^ b
# # a = a ^ b
# # print(a)
# # print(b)
# #
# # ## 7 sum_split_list
# #
# # def list_elems(N):
# #     res = []
# #     while N != 0:
# #         res.append(N % 10)
# #         N = N // 10
# #     return res
# #
# # def sum_split_list(N):
# #     res = []
# #     l = list_elems(N)
# #     sum_n = sum(l)
# #     for i in l:
# #         res.append(sum_n - i)
# #     return " ".join(map(str, res[::-1]))
# #
# #
# # print(sum_split_list(345))
# #
# #
# #
# # ##  8 dict key value number
# # s = "dfghjkl;kjnbvcxbnkvcbjmnbvn"
# # res = {k: s.count(k) for k in s}
# # print(res)
# # d = {}
# # for k, v in enumerate(res):
# #     print(k, v)
# #     if v not in d:
# #         d[v] = [k]
# #     else:
# #         d[v].append(k)
# # print(d)
# #
# # ### 9  how many combination  in a list
# # #
# # # l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # tar = int(input("enter number"))
# # # for i in range(len(l)):
# # #     for j in range(i + 1, len(l)):
# # #         if l[i] + l[j] == tar:
# # #             print([l[i], l[j]], end=" ")
# #
# #
# # ## 10 first n numbers fibinoc series
# # def fib(n):
# #     a = 0
# #     b = 1
# #     res = [a, b]
# #     for i in range(2, n):
# #         c = a + b
# #         res.append(c)
# #         a = b
# #         b = c
# #     return res
# # print(fib(9))
# #
# # #### 11 factorial of a number
# #
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
# #
# #
# # print(factorial(8))
# #
# #
# #
# #
# # def recursion(n):
# #     res = []
# #     while n != 0:
# #         res.append(n)
# #         n = n - 1
# #         recursion(n)
# #     return res
# #
# #
# # print(recursion(5))
# #
# #
# # ##  12 find first n prime numbers
# # n = int(input("enter n:"))
# # c = 2
# # while n != 0:
# #     for i in range(2, c):
# #         if c % i == 0:
# #             break
# #     else:
# #         print(c, end=" ")
# #         n -= 1
# #     c += 1
# #
# # ## 13 find key index position key value
# #
# d = {'a': 2, "b": 3, "c": 4, "d": 3, "e": 3, "k": 1, "p": 0}
# d1 = {}
# for k,v in enumerate(d):
#     print(k, v)
#     if v not in d1:
#         d1[v]=[k]
#     else:
#         [k].append()
# print(d1)
#
# #13.1 to get items in a dictionary
#
# d1 = {}
# for k, v in enumerate(d.items()):
#     print(v)
#
# # 13.2 to get only keys in a dictionary
#
# d = {'a': 2, "b": 3, "c": 4, "d": 3, "e": 3, "k": 1, "p": 0}
#
# d1 = {}
# for k, v in enumerate(d):
#     print(v)
#
# ## 13.3 to get only values in a dictionary
#
# d1={}
# for k,v in enumerate(d):
#     q=d[v]
#     print(q)


#
#
# #### 14 json to dict
# # def json_to_dict(d):
# #     r = d.split(",")
# #     res = []
# #     for i in r:
# #         res.extend(i.strip('{  }  ').split(":"))
# #     d1 = {}
# #     for i in range(0, len(res) - 1, 2):
# #         key, value = res[i].strip('"'), res[i + 1].strip('"')
# #         d1[key] = value
# #     return d
# # d = '{"g":"a","n":"g","a":"d","r":"i"}'
# # print(json_to_dict(d))
#
#
#
#
#
#
# ###  15  is_perfect_number
#
# # def is_perfect_number(n):
# #     divisors = []
# #     for i in range(1, n):
# #         if n % i == 0:
# #             divisors.append(i)
# #     if sum(divisors) == n:
# #         return True
# #     else:
# #         return False
# #
# # print(is_perfect_number(6))
#
#
#
# # ####  16 string values repeting
# # s = "s3b2c3d4j8"
# # res = []
# # for i in range(0, len(s), 2):
# #     res.append(s[i] * int(s[i + 1]))
# # print("".join(res))
#
#
# ### 17 counting list  flat listvalues into single element
# def single(l):
#     res = []
#     for i in l:
#         if type(i) == list:
#             res.extend(i)
#         else:
#             res.append(i)
#     for j in res:
#         if type(j) == list:
#             return single(res)
#     else:
#         return sum(res)
# print(single([1, 2, [2, 3, 4], [2, 3, 4, [4, 5, 6,[2,3]]], 0]))
# #
# # ### 18  second max value in a list
# l = [1, 2, 3, 4, 5, 6, 7]
# maximum = 0
# second_max=0
# for i in range(len(l)):
#     if maximum < l[i]:
#         second_max=maximum
#         maximum = l[i]
# print(second_max)
# #
# ### 19 how to find 3rd highest number
# l = [1, 2, 3, 4, 5, 6, 7]
# max1=0
# max2=0
# max3=0
# for i in l:
#     # Update the maximum value if we find a new maximum
#     if i > max1:
#         max3 = max2
#         max2 = max1
#         max1 = i
#     # Update the second maximum value if we find a new second maximum
#     elif i > max2:
#         max3 = max2
#         max2 = i
#     # Update the third maximum value if we find a new third maximum
#     elif i > max3:
#         max3 = i
#
# print(max2)
# #
#
# #
# # ##### 20 remove duplicate in a neasted list values in a list
#
# l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# res=[]
# for sub_list in l:
#     if sub_list not in res:
#         res.append(sub_list)
# print(res)
#### 20.1 to find only duplacate in a list

# l = [1, 2, 3, 4, 5, 2, 4, 3, 5, 6]
# d = {}
# l1= []
#
# for i in l:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#         if d[i] == 2:
#             l1.append(i)
#
# print(l1)
########## 20.2 it will give only removed  element  in multiple datatype in a list
# from collections.abc import Hashable
#
# l = [1, 2, 3, 4, 4, 3, "1", "2", "1", {"1": "1"}, {"1": "1"}, 5, 6]
# l1 = []
# d = {}
#
# for i in l:
#     # If i is not hashable, it cannot be a dictionary or a set, so we use str() to convert it to a hashable type
#     # If i is hashable, we use i directly as the key in the dictionary
#     key = str(i) if not isinstance(i, Hashable) else i
#
#     if key not in d:
#         d[key] = 1
#     else:
#         d[key] += 1
#         if d[key] == 2:
#             l1.append(i)
#
# print(l1)

#
#
# #### 21 ip="aaabbbaabbcc" op= 3a3b2a2b2c
# # s="aaabbbaabbcc"
# # c=""
# # count=1
# # q=s[0]
# # for i in s[1:]:
# #     if i ==q:
# #         count+=1
# #     else:
# #         c+=str(count)+q
# #         q=i
# #         count=1
# # c+=str(count)+q
# # print(c)
#
# ###  22 all zeros at end op=[1, 2, 3, 4, 5, 0, 0]
#
# l=[1,0,2,3,0,4,5]
#
# # for i in range(len(l)):
# #     if(l[i]==0):
# #         l.append(0)
# #         l.pop(i)
# # print(l)
#
# for i in l:
#     if i==0:
#         l.append(i)
#         l.remove(i)
# print(l)
#
# ### 23 amstrong  number
#
#
# # n=158
# # order=len(str(n))
# # sum=0
# #
# # temp=n
# # while temp>0:
# #     digit=temp%10
# #     sum+=digit**order
# #     temp//=10
# # if n==sum:
# #     print(n,"is a amstrong ")
# # else:
# #     print(n, "is not a amstrong ")
#
#
#
# ### 24 list element in assending order
#
# # l=[1,23,43,67,2,3,78,56]
# # for i in range(len(l)):
# #     for j in range(i+1,len(l)):
# #         if l[i]>l[j]:
# #             l[i],l[j]=l[j],l[i]
# # print(l)
#
#
# #### 25 removing duplicates from list
#
# # l=[1,2,3,2,4,5,2,34,6,4,6]
# #
# # q=[i for j,i in enumerate(l) if i not in l[:j]]
# # print(list(q))
#
#
#
# ### 26 ip=[[1,2,3],[4,5,6],[7,8,9]] op= [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# # l = [[1,2,3],[4,5,6],[7,8,9]]
# # l1 = []
# # l2 = []
# # l3 = []
# # res = []
# #
# # # Iterate over each sublist in l and append the first, second, and third element to l1, l2, and l3 respectively
# # for sublist in l:
# #     l1.append(sublist[0])
# #     l2.append(sublist[1])
# #     l3.append(sublist[2])
# #
# # # Append the elements of l1, l2, and l3 to res as sublists
# # res.append(l1)
# # res.append(l2)
# # res.append(l3)
# #
# # print(res) # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
#
#
# ### 27 find all occurrence element in a list
# # l=["hello","ok","is","hi","ok","hello"]
# #
# # q=[i for i in range(len(l)) if l[i]=="ok"]
# # print(q)
#
# ### 28 occurence element in a list
# #
# # l=["w","e","s","s","s","z","z","s"]
# # q=[i for i,n in enumerate(l) if n=="s"][2]
# # print(q)
#
#
# ### 29 sort a dictionary key
# #
# # d={578:"Lenin gore",901:"nareesh",111:"are"}
# #
# d1=list(d.items())
# for i in range(len(d1)):
#     for j in range(i+1,len(d1)):
#         if d1[i]>d1[j]:
#             d1[i],d1[j]=d1[j],d1[i]
# print(d1)
#
# #### 30 prime numbers
#
# # n=int(input("enter the number"))
# # for i in range(1,n):
# #     for j in range(2,i):
# #         if (i%j==0):
# #             break
# #     else:
# #         print(i)
#
#
# ## 31 swap key to values and values to key
#
# # d={"a":1,"b":2}
# # d1={}
# # for k,v in d.items():
# #     d1[v]=k
# # print(d1)
#
# ### 32  reversa a list values l=["1","2","3"]  ['3', '2', '1']
#
# l=["1","2","3"]
# s1=""
# for i in l:
#     s1=i+s1
# print(list(s1))
#
#
#
# ### 33 first 10 first 10 fibonnaci series
#
# def feb(n):
#     if n<=1:
#         return n
#     else:
#         return (feb(n-1)+feb(n-2))
# n=10
# for i in range(n):
#     print(feb(i))
#
#
# ###  34 only keys reverse in a dict
#
# d={"gfg":4,"is":2,"best":5}
#
# a=list(d.keys())
# b=list(d.values())
# a=a[::-1]
# d1=dict()
# for i,j in zip(a,b):
#     d1[i]=j
# print(d1)
#
#
# ### 35 target number
#
# l=[1,2,3,4,5,6,7,8,9]
# t=10
# for i in l:
#     for j in l:
#         if i+j==10:
#             print(i,j)
#
#
# ####  36 if l=[9,9,9] op = [1, 0, 0, 0]
#
# # l=[9,9,9]
# # x=int("".join(map(str,l)))+1
# # print(list(map(int,str(x))))
#

### 37 getting multiple datatypes values in a list
# l = [1,2,4,3,(1,2),5,6,"1",4.5,7,{"hi":"1"},{1,2}]
#
# l1 = []
# l2 = {}
# l3=[]
#
# for i in l:
#     if isinstance(i, str) or isinstance(i, float) or isinstance(i,tuple) or isinstance(i, set):
#         l1.append(i)
#     elif isinstance(i, dict):
#         l2.update(i)
#     else:
#         l3.append(i)
# print(l1)
# print(l2)
# print(l3)


###  38 l= ['hello', 'world', 'python']    Output: ['HELLO', 'WORLD', 'PYTHON']
# l= ['hello', 'world', 'python']
# # Output: ['HELLO', 'WORLD', 'PYTHON']
#
# q=list(map(lambda x:x.upper(),l))
# print(q)

### 39 lambda function example program filter map reduce function
# s=lambda a,b:a*b
# print(s(2,2))
#
# l=[1,2,3,4,5,6]
# l1=list(filter(lambda i:i%2==0,l))
# print(l1)
#
# l2=list(map(lambda i:i*i,l))
# print(*l2)
#
# from functools import reduce
#
# l3=reduce(lambda a,b:a+b,l)
# print(l3)


###40 l=[1,2,3,4] op={1: 2, 2: 4, 3: 6, 4: 8}

# l=[1,2,3,4]
#
# q={e:e*2 for e in l}
# print(q)

#### 41 dict sort values

# d = {"a": 4, "b": 7, "c": 1, "d": 3}
# d2 = {}
# while d:
#     q = min(d, key=d.get)
#     d2[q] = d.pop(q)
# print(d2)

### 41.1 sort key dictionary
# d = {"a": 4, "b": 7, "c": 1, "d": 3,"z":34,"r":32}
# d2 = {}
# while d:
#     q = min(d)
#     print(q)
#     d2[q] = d.pop(q)
# print(d2)
### 42 l=[1,2,3,4,"are","hi",5,{"hi","fg"}] op=[1,2,3,4,"ARE","HI",5,{"HI","FG"}]

# l=[1,2,3,4,"are","hi",5,{"hi","fg"}]
# op=[1,2,3,4,"ARE","HI",5,{"HI","FG"}]
# l1=[]
#
# for i in l:
#     if isinstance(i,str) or isinstance(i,set):
#         l1.append(str(i).upper())
#     else:
#        l1.append(i)
# print(l1)

##### 43 in a string of list  or set i want to get list or set  out of string

# import re
#
# s = "1,2,3,4,[1,2,3,4]"
# l1 = []
#
# pattern = r"\[[^]]*\]"
# for match in re.finditer(pattern, s):
#     lst = eval(match.group())
#     l1.append(lst)
#
# print(l1)


###44 i want to separate list values and set values in a string


import re

s = "1,2,3,4,[1,2,3,4],{1,2,3,4}"
l1 = []
se = set()
pattern = r"[\[\{][^\[\]\{\}]*[\]\}]"  ## only list then use this pattern r"\[[^]]*\]", if u want to use both then use this pattern   r"[\[\{][^\[\]\{\}]*[\]\}]"
for match in re.finditer(pattern, s):
    obj = eval(match.group())
    if isinstance(obj, list):
        l1.append(obj)
    elif isinstance(obj, set):
        se.update(obj)
print(l1)
print(se)

##### 45 Fibonacci byusing init,iter,next methods
# class Fibonacci:
#     def __init__(self, n):
#         self.n = n
#         self.current = 0
#         self.next = 1
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= self.n:
#             raise StopIteration
#         result = self.current
#         self.current, self.next = self.next, self.current + self.next
#         self.count += 1
#         return result
# q = Fibonacci(10)
# for i in q:
#     print(i)

## 46 find the maximum length of consecutive zero's in a binary string


# WAP to find the maximum length of consecutive zero's in a binary string. Also, find the starting index of the first zero in that substring.


# Input string :   "00010100"
# Expected output :  max length of consecutive zero's is 3, starts at index 0
# Input string :
# Expected output :  max length of consecutive zero's is 4, starts at index 6


# def bin(s):
#     max = 0
#     current_len = 0
#     start_index = -1
#     for i in range(len(s)):
#         if s[i] == "0":
#             current_len += 1
#             if current_len > max:
#                 max = current_len
#                 start_index = i - max + 1
#         else:
#             current_len = 0
#     return (max, start_index)
#
#
# # q="00010100"
# q = "10100100001"
# # qq=bin(q)
# max, start_index = bin(q)
# print(max, start_index)


### 47 If you want to see only the migrations that have not been applied yet, run:


# python manage.py showmigrations --list | grep "\[ \]"


# 48 str1 = "abcde"# if n=5 than output will be "abcde"# if n=3 than "abc"# if n=7 than "abcdeab"if n=11 than "abcdeabcdea"# if n=15 than "abcdeabcdeabcde"

# str1 = "abcde"
# n=int(input("enter str"))
# if n<=len(str1):
#     q=str1[:n:-1]
# else:
#     num=n//len(str1)
#     r=n%len(str1)
#     q=str1*num+str1[:r]
# print(q)


###49 input "my name is nareesh"  output=NAREESH IS NAME MY


s = input("enter str")
l = s.split()
l1 = []
i = len(l) - 1
while i >= 0:
    l1.append(l[i])
    i = i - 1
q = ' '.join(l1).upper()
print(q)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

pdf_file = canvas.Canvas("output.pdf", pagesize=letter)
pdf_file.setTitle("My Python Programs")

with open("program.py", "r") as f:
    content = f.readlines()

line_count = 0  # Counter for the number of lines on the current page
y_position = 750  # Starting y position for the first line of content

for line in content:
    pdf_file.drawString(100, y_position, line.strip())  # Use strip() to remove the newline character
    y_position -= 20  # Move down 20 points for the next line
    line_count += 1

    if line_count == 50:  # Start a new page after 50 lines
        pdf_file.showPage()
        line_count = 0  # Reset the line count
        y_position = 750  # Reset the y position

# If the last page is not filled completely, add a new page to avoid blank space
if line_count > 0:
    pdf_file.showPage()

pdf_file.save()

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

pdf_file = canvas.Canvas("output.pdf", pagesize=letter)
pdf_file.setTitle("My Python Programs")

with open("program.py", "r") as f:
    content = f.readlines()

line_count = 0  # Counter for the number of lines on the current page
y_position = 750  # Starting y position for the first line of content

for line in content:
    pdf_file.drawString(100, y_position, line.strip())  # Use strip() to remove the newline character
    y_position -= 20  # Move down 20 points for the next line
    line_count += 1

    if line_count == 50:  # Start a new page after 50 lines
        pdf_file.showPage()
        line_count = 0  # Reset the line count
        y_position = 750  # Reset the y position

# If the last page is not filled completely, add a new page to avoid blank space
if line_count > 0:
    pdf_file.showPage()

pdf_file.save()



###  50 oops

######### 1 single inheritance
# class P:
#     def m1(self):
#         print("p class")
# class C:
#     def m1(self):
#         print("C class")
#
# c=C()
# c.m1()
# p=P()
# p.m1()




######## 2 multi level inheritan
class P:
    def m1(self):
        print("A")
class C(P):
    def m2(self):
        print("B")
class CC(C):
    def m3(self):
        print("c")

c=P()
c.m1()

q=C()
q.m2()
q.m1()

w=CC()
w.m2()
w.m3()
w.m1()


#### 3 hierarchical inheritance

class P:
    def m1(self):
        print("a")
class C1(P):
    def m2(self):
        print("b")
class C2(P):
    def m3(self):
        print("b1")

c=C1()
c.m1()
c.m2()

q=C2()
q.m3()
q.m1()







###multiple inheritance
class A:
    def method_A(self):
        print("This is method A")

class B:
    def method_A(self):
        print("This is method B")

class C(B,A):
   print(" this method c")


c = C()
c.method_A()

q=B()
q.method_A()

w=A()
w.method_A()

### encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance
# Create a new bank account with account number 123 and balance 1000.
account = BankAccount(123, 1000)

# Deposit 500 into the account.
account.deposit(500)

# Withdraw 200 from the account.
account.withdraw(200)

# Print the current balance.
print("Current balance:", account.get_balance())

### static methoh

class stme:
    @staticmethod
    def add(x,y):
        print("sum",x+y)
    @staticmethod
    def div(x,y):
        print("div",x*y)
    @staticmethod
    def avg(x,y):
        print("avg",(x+y)/2)


stme.avg(5,5)





###51 even odd prime pali


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
def find(l):
    odd=[]
    even=[]
    prime=[]
    pali=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
        is_prime=True
        if i<2:
            is_prime=False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            prime.append(i)
        if str(i)==str(i)[::-1]:
            pali.append(i)
    return {
        "even":even,
        "odd": odd,
        "prime":prime,
        "pali":pali
        }

q=find(l)
print(q)



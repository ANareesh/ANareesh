import collections
import itertools
import random
from functools import reduce

# l=[1,2,3,4,5]
# sum=reduce(lambda x,y:x+y,l)
# print(sum)






#
# l=[1,2,3,4,5]
# mul=reduce(lambda x,y:x*y,l)
# print(mul)

# ls=[1,2,3,4,5,6,7,8]
# sum=sum(ls)
# print(sum)
#
#
# ls=[1,2,3,4,5,8,6,8,7,8]
# for elem in ls:
#     if elem==max(ls):
#         break
# print(elem)


# ls=[1,2,3,4,5,8,6,8,7,8]
# for elem in ls:
#     if elem==min(ls):
#         break
# print(elem)


# ls= ['abc', 'xyz', 'aba', '1221']
# re_list=[elem for elem in ls if len(elem)>=2 and elem[0]==elem[-1]]
# print(re_list)

# ls= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_ls=sorted(ls,key=lambda kv:kv[1])
# print(sorted_ls)

# ls=[1,2,3,45,1,3,4,56,78,1,3,4,5,6,7,89,2,3,4,56]
# #print(set(ls))
# original_ls=[]
# for elem in ls:
#     if elem not in original_ls:
#         original_ls.append(elem)
# print(original_ls)

# l=[1,2,3,4]
# key=int(input())
# if key in l:
#     print(True)
# else:
#     print(False)


# ls=input().split(" ")
# num=int(input())
# num_list=[]
# count=0
# for elem in ls:
#     if len(elem)>=num:
#         num_list.append(elem)
#         count+=1
# print(num_list)
# print(count)

# num_list=[elem for elem in input().split(" ") if len(elem)>=3]
# print(num_list)


# def com_member(list1, list2):
#     for elem in list1:
#         if elem in list2:
#             return True
#     return False
#
#
# print(com_member([1, 2, 3, 4, 5], [6, 3, 8, 9]))

# def odd_num(list):
#     odd_list=[]
#     for elem in list:
#         if elem%2==1:
#             odd_list.append(elem)
#             return odd_num(odd_list)
# res=odd_num([1,2,3,4,5,6,7,8,9])
# print(res)
#
#
# ls= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(ls[1:4])

# ls=[1,2,3,4,5,6,7,8,9]
# odd_list=[elem for elem in ls if elem%2==1]
# print(odd_list)

#
# ls=[1,2,3,4,5,6,7,8,9]
# odd_list=list(filter(lambda elem:elem%2==1,ls))
# print(odd_list)


#
# sqare_list=[elem**2 for elem in range(1,31) ]
# print(sqare_list[0:5],sqare_list[25:])
# from random import shuffle
#
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)

# ls = [1, 3, 5, 7, 9]
# ls1 = [1, 2, 4, 6, 7, 8]
# s=set(ls)
# s1=set(ls1)
#
# x=s.difference(s1)
# x1=s1.difference(s)
# total_difference=x1.union(x)
# print(total_difference)

# res = ls + ls1
# r = {k: res.count(k) for k in res}
# res = [k for k, v in r.items() if v == 1]
# print(res)

# {2, 3, 4, 5, 6, 8, 9}

# ls = [1, 3, 5, 7, 9]
# for elem in enumerate(ls):
#     print('(index,', 'elem):', elem)

# for i in range(0,len(ls)):
#     print(i,ls[i])

# for i in enumerate(ls):
#     print(i)


# ls=[1, 2, 4, 6, 7, 8]
# key=int(input())
# x=ls.index(key)
# print(x)

# print(list(itertools.permutations([1,2,3])))


# shallow_list=[1,2,3],[4,5,6],[7,8,9]
# flatend_list=[]
# res_list=[]
# for elem in shallow_list:
#     flatend_list.append(elem)
# for list in flatend_list:
#         res_list.extend(list)
# print(res_list)

# ls=[1,2,3,4,5]
# ls1=[6,7,8,9]
# ls2=[]
# for elem in ls:
#     ls2.append(elem)
# for elem in ls1:
#     ls2.append(elem)
# print(ls2)
#
# ls=[1,2,3,4,5]
# ls1=[6,7,8,9]
# ls2=ls+ls1
# print(ls2)

#
# ls=[45,60,72,30,1,2,80,3,4,5,-5,-8,-10,50,60,76]
# p=min(ls)
# res=[]
# for elem in ls:
#     if elem==p:
#         res.append(elem)
# print(res)


# ls = [45, 60, 72, 30, 1, 2, 80, 3, 4, 5, -5, -8, -10, 50, 60, 76]
# sorted_ls=sorted(ls)
# print(sorted_ls)
# second_max=sorted_ls[-2]
# second_min=sorted_ls[1]
# print(second_min)
# print(second_max)

# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))
#


# lst=list(map(int,input().split(" ")))
# lst=input().split(" ")
# print(lst)
# cyclic_lst=lst*2
# print(cyclic_lst)
# for i in range(1,len(lst)):
#    print(" ".join(cyclic_lst[i:i+len(lst)]))

# l = list(map(int, input("enter integers").split(" ")))
# n = int(input("enter number"))
# l1 = l * 2
# # for i in range(n, len(l)):
# print(l1[n:n + len(l)])

# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)


# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# d={}
# for elem in my_list:
#     if elem not in d:
#         d[elem]=1
#     else:
#         d[elem]+=1
# print(d)


# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# unique_list=[]
# for elem in my_list:
#     if elem not in unique_list:
#         unique_list.append(elem)
# print(unique_list)

# lst=[]
# count=0
# for elem in range(40,100,10):
#     lst.append(elem)
#     count+=1
# print(count)

# print(list((list(range(1,10)),list(range(10,20)),list(range(20,30)))))


# print(dict(x=list(range(1, 10)), y=list(range(10, 20)), z=list(range(20, 30))))

# ls= ['p', 'q']
# n=int(input())
# res=[]
# i=1
# while i<=n:
#    x=(i,'p','q',i)
#    res.append(x)
# print(res)
# i+=1


# n = int(input())
# res = []
# for i in range(1, n + 1):
#     x = [str(i) + 'p', 'q' + str(i)]
#     res.extend(x)
# print(res)

# ls=list(map(int,input().split(",")))
# ls1=list(map(int,input().split(",")))
# res=[]
# for elem in ls:
#     if elem in ls1:
#         res.append(elem)
# print(res)

# ls=[1,2,3,4,5,6,7]
# print(random.choice(ls))


# ls=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# print(list(ls[0::3]),(ls[1::3]),(ls[2::3]))


# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# my_list.sort(key=lambda e:e['key']['subkey'],reverse=True)
# print(my_list)
# res = []
# maximum = 0
# for i in my_list:
#     print(i['key']['subkey'])
#     if i['key']['subkey'] > maximum:
#         maximum = i
#         res.insert(0, maximum)
# print(res)
# l = [1, 2, 3, 4, 5, 6]
# for i in l:
#     l.remove(i)
#     l.insert(0,i)
# print(l)
# # ls1 = []
# # for i in range(len(ls) - 1):
# #     ls[i], ls[i + 1] = ls[i + 1], ls[i]
# # print(ls)
# l[0::2], l[1::2] = l[1::2], l[0::2]
# print(l)
#
#
# ls= [11, 33, 50]
# res=""
# for i in ls:
#     res=res+str(i)
# x=int(res)
# print(x)
# print(type(x))


# l=[]
# i=0
# while i>=0:
#     l.append(i)
# print(l)


# ls=[1,2,3,4,5,6,7,8]
# ls1=[]
# for i in range(1,len(ls)-1):
#     ls1.append((i+(i+1))/2)
# print(ls1)

# ls=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# ls1=[('red', 'green'), ('orange', 'pink')]
# s1=set(ls)
# s2=set(ls1)
# x=s1.intersection(s2)
# print(x)

#
# ls=[1234, 1522, 1984, 19372, 1000, 2342, 7626]
# ls1=[]
# for index,value in enumerate(ls):
#     if value<3000:
#         pass
#     else:
#         ls1.append(index)
# print(ls1)


# ls=['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy',' ']
# ls1=[]
# for i in range(len(ls)-1):
#     if ls[i]==" " and ls[i+1]==" ":
#         continue
#     else:
#         ls1.append(ls[i])
# ls1.append(ls[-1])
# print(ls1)


# ls = [1234, 122, 1984, 19372, 200]
# ls1 = list(map(str, ls))
# for num in ls1[1:]:
#     if ls1[0][0] != num[0]:
#         print(False)
#         break
# else:
#     print(True)

# ls=[1234, 122, 1984, 19372, 100]
# def isFirstChar_equel(lst):
#     for num in lst[1:]:
#         if lst[0][0]!=num[0]:
#             return False
#     return True
# lst=list(map(str,ls))
# res=isFirstChar_equel(lst)
# print(res)


#
# lst=[1, None, 5, 4, None, 0, None, None]
# lst1=[]
# for i in range(len(lst)):
#     if lst[i]==None:
#         lst1.append(i)
# print(lst1)

#
# lst=['1', '2', '3', '4', '5', '6', '7', '8']
# res=[]
# for i in range(0,len(lst)-1,2):
#     res.append(lst[i]+lst[i+1])
# print(res)

#
# s='https://www.w3resource.com/python-exercises/list/'
# ls= ['.com', '.edu', '.tv']
# for elem in ls:
#     if elem in s:
#         print(True)
#         break
# else:
#     print(False)

#
# lst=[1, 2, 3, 4, 5, 6]
# lst1=[]
# for i in range(len(lst)-1):
#     lst1.append([lst[i],lst[i+1]])
# print(lst1)
# res=[]
# for i in range(0,len(lst)-1,2):
#     print(lst[i:i+2])

# l1=[1, 2, 3, 4, 15, 6]
# l2=[7, 8, 5, 7, 10, 12]
# l3=[]
# for i,v in enumerate(l1):
#     if v in l2:
#         l3.append(i)
# print(l3)

# i=int(input())
# j=int(input())
# ls=['red', 'green', 'white', 'black', 'orange']
# ls[i],ls[j]=ls[j],ls[i]
# print(ls)


# ls=['red', 'green', 'white', 'black']
# ls1=[]
# ls2=[]
# for index,value in enumerate(ls):
#     print(value,index)
#     ls1.append(index)
#     ls2.append(value)
# for i,j in zip(ls1[::-1],ls2[::-1]):
#     print(i,j)

#
# ls=[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# ls1=sorted(ls,key=lambda kv:kv[2])
# print(ls1)


# ls = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# max_len = len(max(ls, key=len))
# for sub_list in ls:
#     sub_list.extend([0] * (max_len - len(sub_list)))
#     print(ls)
# res = []
# for tuple in zip(*ls):
#     res.append(sum(tuple) / len(tuple))
# print(res)

# l1=[2, 3, 5, 8, 7, 2, 3]
# l2=[4, 3, 9, 0, 4, 3, 9]
# l3=[2, 1, 5, 6, 5, 5, 4]
# l=[]
# for sub_list in (l1,l2,l3):
#     l.extend(sub_list)
# print(max(l),min(l))


# l=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# ls=[]
# for tuple in l:
#     ls.append(" ".join(tuple))
# print(ls)


# ls=[]
# for tuple in l:
# for elem in tuple:
#         ls.append(elem)
# print(ls)
# ls1=[]
# for i in range(0,len(ls)-1,2):
#     ls1.append(ls[i]+' '+ls[i+1])
# print(ls1)

# res=[" ".join(tuple) for tuple in l]
# print(res)


# l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# l[6:10],l[1:3]=l[1:3],l[6:10]
# l[1:3],l[4:6]=l[4:6],l[1:3]
# print(l)

#
# l1=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# l2=[]
# for list in l1:
#     for elem in list:
#         l2.append(elem)
# l3=[]
# for elem in l2:
#     if elem not in l3:
#         l3.append(elem)
# print(l3)


# lst=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# lst1=[]
# for list in lst:
#     lst1.append(sum((list)))
# max_sum=max(lst1)
# min_sum=min(lst1)
# for list in lst:
#     if sum(list)==max_sum:
#         print(list,end="")
# for list in lst:
#     if sum(list)==min_sum:
#         print(list)

# i=int(input())
# lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# cyclic_list=lst*2
# for i in range(i,len(lst)):
#     print(cyclic_list[i:i+len(lst)])
#     break


# ls=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# min_list=(min(ls,key=len))
# for i in range(len(min_list)):
#     temp=[]
#     for sub_list in ls:
#         temp.append(sub_list[i])
#     print(temp)

# ls=[3, 40, 41, 43, 74, 9]
# sorted_ls=sorted(ls)
# min_num=[]
# for elem in sorted_ls:
#     min_num.append(str(elem))
# x="".join(min_num)
# print((int(x)))


# ls=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# res=[]
# for i in range(len(ls)):
#     temp=[]
#     for sub_list in ls:
#         try:
#              temp.append(sub_list[i])
#         except:
#             pass
#     print(temp)
#     res.append(sum(temp)/len(temp))
# print(res)


#
# n=int(input())
# x=int(input())
# l=list(map(int,input().split(",")))
# # i=n
# # while i<len(l):
# #     l.insert(i,x)
# #     i+=n+1
# # print(l)
#
# l.insert(n,x)
# print(l)


# def insert_value(l,n,x):
#     i=n
#     while i<len(l):
#         l.insert(i,x)
#         i+=n+1
#     return l
# n=int(input())
# x=int(input())
# l=list(map(int,input().split(",")))
# res=insert_value(l,n,x)
# print(res)

# n=int(input())
# x=int(input())
# l=list(map(int,input().split(",")))
# for i in range(n,len(l),4):
#     l.insert(i,x)
# print(l)


# l=[[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# l1=[]
# res=""
# for sub_list in l:
#     temp=set(sub_list)
#     l1.append(temp)
# print(l1)
# for sub_set in l1:
#  res=(l1[0].intersection(*l1))
#  break
# print(list(res))


# l1=[1,2,3,4,5,6,7]
# l2=[1,2,3,4,5,6,7]
# # sum_list=[x+y for x,y in zip(l1,l2)]
# # print(sum_list)
#
# sum_list=[x/y for x,y in zip(l1,l2)]
# print(sum_list)

#
# l=[(2, 3), (2, 4), (0, 6), (7, 1)]
# sorted_list=sorted(l,key=lambda kv:kv[0])
# print([sorted_list[0],sorted_list[-1]])

# l=[3, 8, 9, 4, 5, 0, 5, 0, 3]
# n=int(input())
# l1=[]
# for i in l:
#     l1.append(i+n)
# print(l1)


# l=['a', 'b', 'c', 'd', 'e', 'f', 'g']
# n=int(input())
# m=int(input())
# l1=[]
# for i in range(len(l)):
#     if i in (n,m):
#         l1.append(n*m)
#     else:
#         l1.append(l[i])
# print(l1)


#
# l=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# n=int(input())
# print(l[:-n])


# l1=['0', '1', '2', '3', '4']
# l2=['red', 'green', 'black', 'blue', 'white']
# l3=['100', '200', '300', '400', '500']
# res=[]
# for i,j,k in zip(l1,l2,l3):
#     res.append(i+j+k)
# print(res)


#
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# n=int(input())
# x=input()
# i=n
# while i<len(l):
#     l.insert(i,x)
#     i+=n+1
# print(l)

#
# def spitting_into_chr(l):
#  temp=""
#  res=[]
#  for word in l:
#     temp+=word
#  for ch in temp:
#     res.append(ch)
#  return res
# l=input().split(",")
# res=spitting_into_chr(l)
# print(res)


#
# l=[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# i=0
# while i<len(l):
#     for elem in l[i]:
#         print(elem,sep="")
#     i+=1

# l=[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# for i,j,k in zip(*l):
#     print(i,j,k)
#
# l=['Red', 'Maroon', 'Yellow', 'Olive']
# l1=[]
# for word in l:
#     l1.append(list(word))
# print(l1)


# l=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# l1=[]
# for ch in l:
#     if ch!=None:
#         l1.append(ch)
# print(l1)


#
# l=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# n=int(input())
# l1=[]
# for i in range(0,len(l),n):
#     l1.append(list(l[i:i+n]))
# print(l1)


# l=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# c=0
# for i in l:
#     if i%2==0 and i>45:
#         c+=1
# print(c)

#
# l=[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# n=int(input())
# for i,v in enumerate(l):
#     if v>n:
#      print(i)
#      break


# l=[1,2,3,4,5,4,6,7,3,8]
# c=0
# for i in range(len(l)-1):
#     try:
#       if l[i]>=l[i+1]:
#         l.pop(i+1)
#         c+=1
#     except:
#         pass
# print(c)
# if c<2:
#         print(True)
# else:
#     print(False)

#
# l=[3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# l1=[]
# c=0
# for i in range(len(l)):
#     if l[i]%2==0:
#         c+=1
#     else:
#         l1.append(l[i])
#     if c<=4:
#         pass
#     else:
#         l1.append(l[i])
# print(l1)


# n=[]
# n+=5*["7"]
# print(n)

# n=[1,2,3,4]
# n+=5*['5']
# print(n)

# n=[]
# n.append(5*[[1,2,3,4]])
# print(n)

# n=[[1,2,3,]]
# n.append(4*[[4,5,6]])
# print(n)

#
# l=[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# l1=[]
# for k,v in l:
#     l1.append(v)
# print(l1)
# print((max(l1),min(l1)))


# * l=[2, 4, 7, 0, 5, 8]
# l1=[2, 5, 8]
# l2=[0, 1]
# l3=[3, 3, -1, 7]
# l4=[]
# for list in (l,l1,l2,l3):
#     l4.append(list)
# l5=[]
# for i in zip(*l4):
#     l5.append(i)
# print(l5)


# * l=[0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
# d={}
# k=int(input())
# v=int(input())
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for k,v in d.items():
#     if v in d[k]:
#         print(True)
# else:
#     print(False)

# l1=[1, 3, 5, 7, 9, 11]
# l2=[0, 2, 4, 6, 8, 10]
# l1.extend(l2)
# print(sorted(l1))

#
# l=[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# n=int(input())
# i=int(input())
# l1=[]
# for i in range(i,n+1):
#     l1.append(l[i])
# print((max(l1),min(l1)))

#
# l=[['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# print(l[::-1])


# l=['red', 'green', 'blue', 'white', 'black', 'orange']
# l1=[]
# for word in l:
#     if word=='white' or word=='orange':
#         continue
#     else:
#         l1.append(word)
# print(l1)

#
# l=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# l1=[]
# d={}
# for sub_list in l:
#     for elem in sub_list:
#         l1.append(elem)
# for elem in l1:
#     if elem not in d:
#         d[elem]=1
#     else:
#         d[elem]+=1
# print(d)

#
# l=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# for i,j,k in zip(*l):
#     print(i+j+k)


# l=[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# l1=[]
# for elem in l:
#     if elem !=[]:
#         l1.append(elem)
# print(l1)

#
# l=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# l1=[]
# for elem in l:
#     l1.append(int(elem))
# print(sorted(l1))


# l=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# str_list=[]
# int_list=[]
# l1=[]
# for ch in l:
#     if type(ch)==str:
#         str_list.append(ch)
#     else:
#         int_list.append(ch)
# sorted_int=sorted(int_list)
# sorted_str=sorted(str_list)
# for elem in sorted_int:
#     l1.append(elem)
# for elem in sorted_str:
#     l1.append(elem)
# print(l1)

#
# l=[1, 3, 5, 7, 4, 1, 6, 8]
# for i in range(len(l)-1):
#     if (l[i]%2==0 and l[i+1]%2==1):
#         print((l[i],l[i+1]))


# l=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# l1=[]
# for word in l:
#     if word not in l1:
#         l1.append(word)
# print(l1)


# l=[1, 1, 2, 3, 3, 4, 4, 5]
# l1=[]
# for i in range(len(l)-1):
#     l1.append((l[i],l[i+1]))
# print(l1)

#
# l1=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# l2=[1, 1, 2, 4, 5, 6]
# s1=set[l1]
# s2=set(l2)
# g=s2.symmetric_difference(s1)
# print(g)

# l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# l1=[]
# for sub_list in l:
#     l1.append(sub_list[::-1])
# print(l1)
#
# l=[12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# for i in range(len(l)):
#     if l[i]==max(l):
#       print((i))
# for i in range(len(l)) :
#     if l[i]==min(l):
#         print((i))

#
# l=[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# i=int(input())
# n=int(input())
# sum=0
# for i in range(i,n+1):
#     sum+=l[i]
# print(sum)

#
# list1= [1, 2, 3, 4, 5, 6, 7]
# list2= [10, 20, 30, 40, 50, 60, 70]
# list3= [100, 200, 300, 400, 500, 600, 700]
# l=[]
# res=[]
# for list in (list1,list2,list3):
#     l.append(list)
# for i,j,k in zip(*l):
#     print(i,j,k,end=" ",sep=" ")

#
# l=[10, 20, 30, 40, 20, 50, 60, 40]
# l1=[]
# res=1
# for i in l:
#     if i not in l1:
#         l1.append(i)
# for elem in l1:
#     res*=elem
# print(res)


# l=[(2, 7), (2, 6), (1, 8), (4, 9)]
# l1=[]
# res=[]
# for sub_tuple in l:
#     for elem in sub_tuple:
#         l1.append(elem)
# for i in range(0,len(l1)-1,2):
#     res.append(l1[i]*l1[i+1])
# print((max(res),min(res)))


# l=['Red', 'Green', 'Blue', 'White', 'Black']
# l1=[]
# for word in l:
#     l1.append(word[::-1])
# print(l1)

#
# l=['red', 'black', 'white', 'green', 'orange']
# print(l[::2])

#
# *l=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# l1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# l2=[]
# for x,y in zip(l,l1):
#     z=[x,y]
#     l2.append(z)
# print(l2)
# l3=[]
# for i in range(len(l1)-1):
#     print(l1[i].extend(l[i][i+1]))


# #l=[10, 20, 4, 5, 'b', 70, 'a']
# l=[10, 20, -4, 5, -70]
# i=0
# sum=0
# for elem in l:
#   for i in str(elem):
#       try:
#           sum+=int(i)
#       except:
#           pass
# print(sum)


#
# l=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# li=[]
# i=0
# for sub_list in l:
#
# for i in zip(*l):
#     print([i])


# l1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# l2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# for i in range(len(l2)):
#     l1[i].extend(l2[i])
# print(l1)


#
# l1=[2, 4, 7, 0, 5, 8]
# l2=[2, 5, 8]
# l3=[0, 1]
# l4=[3, 3, -1, 7]
# l=[]
# res=[]
# #max_len=
# for list in (l1,l2,l3,l4):
#     l.append(list)
# max_len=len(max(l,key=len))
# for i in range(max_len):
#     try:
#             res.append(l1[i])
#     except:
#         pass
#     try:
#         res.append(l2[i])
#     except:
#         pass
#     try:
#         res.append(l3[i])
#     except:
#         pass
#     try:
#         res.append(l4[i])
#     except:
#         pass
# print(res)


#
# l1=[2, 4, 7, 0, 5, 8]
# l2=[3, 3, -1, 7]
# res_list=[]
# for x,y in zip(l1,l2):
#     try:
#         res_list.append(x+y)
#     except:
#         pass
# print(res_list)


# l1=[2, 4, 7, 0, 5, 8]
# l2=[3, 3, -1, 7]
# l=[]
# res=[]
# for list in (l1,l2):
#     l.append(list)
# for i in range(len(l1)):
#     temp=[]
#     for sub_list in l:
#         try:
#             temp.append(sub_list[i])
#         except:
#             pass
#     print(temp)
#     res.append(sum(temp))
# print(res)


# ls=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# res=[]
# for i in range(len(ls)):
#     temp=[]
#     for sub_list in ls:
#         try:
#              temp.append(sub_list[i])
#         except:
#             pass
#     print(temp)
#     res.append(sum(temp)/len(temp))
# print(res)


#
# l1=[2, 4, 7, 0, 5, 8]
# l3=l1[::-1]
# l2=[3, 3, -1, 7]
# l4=l2[::-1]
# l=[]
# res=[]
# for list in (l3,l4):
#     l.append(list)
# for i in range(len(l3)):
#     temp=[]
#     for sub_list in l:
#         try:
#             temp.append(sub_list[i])
#         except:
#             pass
#     print(temp)
#     res.append(sum(temp))
# print(res[::-1])

# l=['red', 'black', 'white', 'green', 'orange']
# sub_string=input()
# for word in l:
#     if sub_string in word:
#         print(True)
#         break
# else:
#     print(False)

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res=[]
# for i in range(len(l)-1):
#     res.append(l[i+1]-l[i])
# print(res)


# l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1= [2, 4, 6, 8]
# for i in range(len(l1)):
#     for elem in l:
#         if elem==l1[i]:
#             l.remove(elem)
# print(l)


# l=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# sorted_l=sorted(l,key=lambda kv:kv[2])
# print(sorted_l)


# l=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# n=int(input())
# for i in range(n,len(l)-1):
#     temp=[]
#     for sub_tuple in l:
#         temp.append(sub_tuple[n])
# print(temp)


# l=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# l1=[]
# for sub_dict in l:
#     if sub_dict not in l1:
#         l1.append(sub_dict)
# print(l1)


#
# l=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# l1=[]
# for i in range(len(l)-1):
#    if l[i]>l[i+1]:
#        l1.append(l[i+1])
# if len(l1)==0:
#     print(True)
# else:
#     print(False)


# l=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# maximum=max(d.values())
# for k,v in d.items():
#      if v==maximum:
#       print(k)
#       break


# l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# l1=[]
# n=int(input())
# for i in range(n,len(l)):
#     temp=[]
#     for elem in l:
#         l1.append(elem[n])
# print(l1)


#
# l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# res=[]
# l1=[]
# for i in range(len(l)):
#     temp=[]
#     for elem in l:
#         temp.append(elem[i])
#     res.append(temp)
#
# # print(res)
#
# for i in zip(*l):
#     res.append(list(i))
# print(res)

#
# l=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# c=0
# for ch in l:
#     if type(ch)==int:
#         c+=1
# print(c)

#
# l1=[1, 1, 3, 4, 4, 5, 6, 7]
# l2=[0, 1, 2, 3, 4, 4, 5, 7, 8]
# l_len=len(l1)+len(l2)
# print(l_len)
# l=[]
# res=[]
# for list in (l1,l2):
#     l.append(list)
# for i in range(len(l2)):
#     temp=[]
#     for sub_list in l:
#         try:
#           temp.append(sub_list[i])
#         except:
#             pass
#     res.append(sum(temp))
# print(sum(res)/l_len)

#
# l=[1, 1, 3, 4, 4, 5, 6, 7]
# res=[]
# for i in range(len(l)-1):
#     res.append(l[i+1]-l[i])
# print(res)


# l=[1, 1, 3, 4, 4, 5, 6, 7]
# res=[]
# for i in range(len(l)-1):
#     if l[i]==l[i+1]:
#         res.append(l[i])
# print(res)
#
#
# l=['Python', 'list', 'exercises', 'practice', 'solution']
# n=int(input())
# res=[]
# for word in l:
#     if len(word)==n:
#         res.append(word)
# print(res)
#
# l=['Python', 3, 2, 4, 5, 'version']
# res=[]
# for ch in l:
#     if type(ch)==int:
#         res.append(ch)
# print((max(res),min(res)))

#
# l=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# len_1=[]
# len_m=[]
# for sub_list in l:
#     if len(sub_list)<=1:
#         len_1.append(sub_list)
#     else:
#         len_m.append(sub_list)
# sorted_1=sorted(len_1)
# sorted_m=sorted(len_m,key=lambda kv:kv[0])
# print(sorted_1+sorted_m)


# l=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# d={}
# for ch in l:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# print(d)

# l=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# l1=[]
# n=int(input())
# for sub_list in l:
#     l1.extend(sub_list)
# count_n=l1.count(n)
# print(count_n)

#
# l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# l1=[]
# for sub_list in l:
#     l1.append((len(sub_list),sub_list))
# print(max(l1),min(l1))


# l=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# count=0
# l1=[]
# for sub_list in l:
#     l1.append(sub_list)
#     count+=1
# print(count)


# l1=[[1, 3], [5, 7], [9, 11]]
# l2=[[2, 4], [6, 8], [10, 12, 14]]
# for i in range(len(l1)):
#     l1[i].extend(l2[i])
# print(l1)

#
# l= [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# l1=[]
# res=[]
# for i in l:
#     l1.append(int(i))
# for j in l1:
#     if j>=4 and j<=22:
#         res.append(j*5)
# print(sorted(res))

#
# l=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# l1=[]
# for i in l:
#     l1.append(int(i))
# print(sum(l1)*len(l))


# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(l)-1):
#     print([l[i],l[i+1]],end="")

#
# l=[1, 1, 2, 3, 4, 4, 5, 1]
# k=int(input())
# v=int(input())
# l.insert(k,v)
# print(l)


# l=[1, 1, 2, 3, 4, 4, 5, 1]
# k=int(input())
# l.pop(k)
# print(l)

# l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# res=[]
# temp=[]
# for i in range(len(l)-1):
#     if l[i]!=l[i+1]:
#         pass
#     else:
#        temp.append(l[i])
#     print(temp)


# l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# res=[]
# for i in range(len(l)-1):
#     try:
#      if l[i]!=l[i+1]:
#         res.append(l[i])
#     except:
#         pass
# res.append(l[-1])
# print(res)


# l= [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# l1=[]
# l2=[]
# for i in l:
#     if type(i)==int:
#         l1.append(i)
#     else:
#        l2.append(i)
# res=[]
# for sub_list in l2:
#     for i in sub_list:
#         res.append(i)
# l1.extend(res)
# print(sorted(l1))


# l=  [{},{},{}]
# c=0
# for sub_dict in l:
#     if len(sub_dict)==0:
#         c+=1
# if c==len(l):
#     print(True)
# else:
#     print(False)

#
#
# l=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# s=input()
# i=int(input())
# res=[]
# for word in l:
#     if word[i]==s:
#         res.append(word)
# print(res)


# l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# res=[]
# for sub_list in l:
#     if sub_list not in res:
#         res.append(sub_list)
# print(res)

# l=[10, 20, 30]
# l1=[40, 50, 60]
# l1.extend(l)
# print(l1)

#
# l=[1,2,3,4,5,6,7,8,9]
# n=int(input())
# res=[]
# for i in l:
#     if i>n:
#         res.append(i)
# print(res)

# l=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# max_sum=max(map(sum,l))
# for sub_list in l:
#     if max_sum==sum(sub_list):
#         print(sub_list)


# l=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# expected_list=[i for i in l if i!=0]+[i for i in l if i==0]
# print(expected_list)

# l1= [1, 3, 5, 7, 9, 10]
# l2=[2, 4, 6, 8]
# l1[-1:]=l2
# print(l1)

#
# l = [1, 2, 3, 4, 5, 6, 7]
# maximum = 0
# second_max=0
# for i in range(len(l)):
#     if maximum < l[i]:
#         second_max=maximum
#         maximum = l[i]
# print(second_max)
#
#
# def flat_list(l):
#     res = []
#     for i in l:
#         if type(i) == list:
#             res.extend(i)
#         else:
#             res.append(i)
#     for j in res:
#         if type(j) == list:
#             return flat_list(res)
#     else:
#         return sum(res)
#
#
# print(flat_list([1, 2, [2, 3, 4], [2, 3, 4, [4, 5, 6,[2,3]]], 0]))

# def single_digit(n):
#     sum = 0
#     for i in n:
#         sum += int(i)
#     if len(str(sum)) == 1:
#         return sum
#     else:
#         return single_digit(str(sum))
#
#
# print(single_digit('12345'))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
# for i in l:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")

# s = 12345
# i = 0
# val=0
# while i < s:
#     res = s % 10
#     val=val*10+res
#     s = s // 10
#     print(val)


# s=input("enter value")
# res=[]
# if len(s) % 2 == 1:
#     print(len(s))
#     for i in s:
#         if len(res)==0 and i in "}])":
#             print(len(s))
#         elif i in '({[':
#             res.append(i)
#         elif i=='}' and res[-1]=='{'  :
#             res.pop()
#         elif i==')' and res[-1] =="(" :
#             res.pop()
#
#         elif i==']' and res[-1]=='[' :
#             res.pop()
# if len(res)==0:
#         print(0)
# else:
#         print(len(res))
#
# a = int(input("Enter the terms"))
# f = 0  # first element of series
# s = 1  # second element of series
# if a <= 0:
#     print("The requested series is")
# else:
#     print(f, s, end=" ")
#     print("________________________________________________________")
#     for x in range(2, a):
#         # print(x)
#         next = f + s
#         print(next, end=" ")
#         f = s
#         s = next
#
# s = "s3b2c3d4j8"
# res = []
# for i in range(0, len(s), 2):
#     res.append(s[i] * int(s[i + 1]))
# print("".join(res))


# n = 6
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         fact = n * factorial(n-1)
#         return fact
#
#
# print(factorial(1))

# def factorial(d):
#     fact = 1
#     for i in range(1, d + 1):
#         fact *= i
#     return fact
#
#
# def is_strong_number(n):
#     a = n
#     i = 0
#     stg_num = 0
#     while i < n:
#         d = n % 10
#         res = factorial(d)
#         stg_num = stg_num + res
#         n = n // 10
#     if stg_num == a:
#         print(True)
#     else:
#         print(False)
#
#
# # is_strong_number(145)


# def count(n):
#     c = 0
#     i = 0
#     while i < n:
#         d = n % 10
#         c += 1
#         n = n // 10
#     return c
#
#
# def is_am_strong_number(n):
#     a = n
#     c = count(n)
#     i = 0
#     sum_n = 0
#     while i < n:
#         d = n % 10
#         res = d ** c
#         sum_n += res
#         n = n // 10
#     if sum_n == a:
#         print(True)
#     else:
#         print(False)
#
#
# is_am_strong_number(153)

#
# def is_perfect_number(n):
#     res = 0
#     for i in range(1, n):
#         if n % i == 0:
#             res += i
#     if res == n:
#         print(True)
#     else:
#         print(False)
#
#
# is_perfect_number(99999999999)
# def json_to_dict(d):
#     r = d.split(",")
#     res = []
#     for i in r:
#         res.extend(i.strip('{  }  ').split(":"))
#     d1 = {}
#     for i in range(0, len(res) - 1, 2):
#         key, value = res[i].strip('"'), res[i + 1].strip('"')
#         d1[key] = value
#     print(d1)
#
#
# d = '{"g":"a","n":"g","a":"d","r":"i"}'
# json_to_dict(d)

# d = {'a': 2, "b": 3, "c": 4, "d": 3, "e": 3, "k": 1, "p": 0}
# d1 = {}
# for k,v in enumerate(d):
#     print(k,v)
# if v not in d1:
#     d1[v]=[k]
# else:
#     [k].append()


# n = int(input("enter n:"))
# c = 2
# while n != 0:
#     for i in range(2, c):
#         if c % i == 0:
#             break
#     else:
#         print(c, end=" ")
#         n -= 1
#     c += 1


# n = 11

# while n != 0:
#     print(n, end=" ")
#     n -= 1

# n = 123
# while n != 0:
#     res = n % 10
#     print(res, end="")
#     print(type(res))
#     n = n // 10
#
# n = 121
# p = n
# res = 0
# while n != 0:
#     r = n % 10
#     res = res * 10 + r
#     n = n // 10
# if p == res:
#     print(True)
# else:
#     print(False)

# n = 10
# p=n
# sum_n = 0
# while n != 0:
#     r = int(input("enter number"))
#     sum_n += r
#     n -= 1
# avg = sum_n / p
# print(avg)

# l=[]
# for i in range(2,200):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(len(l[0:10]))
#
# def recursion(n):
#     res = []
#     while n != 0:
#         res.append(n)
#         n = n - 1
#         recursion(n)
#     return res
#
#
# print(recursion(11))

#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(1))


# def fib(n):
#     a = 0
#     b = 1
#     res = [a, b]
#     for i in range(2, n):
#         c = a + b
#         res.append(c)
#         a = b
#         b = c
#     return res
#
#
# print(len(fib(100)))


# class calculator:
#     def __init__(self,op,*args,):
#         self.args=args
#

# def sum_n(*args):
#     return sum(args)
#
#
# print(sum_n(1,2,3,4,5,6))
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tar = int(input("enter number"))
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] == tar:
#             print([l[i], l[j]], end=" ")


#
from itertools import combinations


#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 10
# res = []
# for i in range(len(l)):
#     print(i)
#     print("____________________________________________")
#     for tup in combinations(l, i):
#         # print(tup)
#         if sum(tup) == total:
#             res.append(list(tup))
# # print(res)
#
# from itertools import combinations
#
#
# class Solution:
#     def combinationSum(self, candidates, target):
#
#         res = []
#         for i in range(len(candidates)):
#             for tup in combinations(candidates, i):
#                 if sum(tup) == target:
#                     res.append(list(tup))
#         return res
#
#
# candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 10
# obj = Solution()
# print(obj.combinationSum(candidates, target))

# s = "dfghjkl;kjnbvcxbnkvcbjmnbvn"
# res = {k: s.count(k) for k in s}
# print(res)
# d = {}
# for k, v in enumerate(res):
#     print(k, v)
#     if v not in d:
#         d[v] = [k]
#     else:
#         d[v].append(k)
# print(d)
# n = "1234"
# l = list(n)
# res = []
# for i in range(len(l)):
#         l.remove(l[i])
#         res.append(l)
#         l = list(n)
# max_elem = max([int("".join(elem)) for elem in res])
# print(max_elem)


# N=int(input("enter number"))
# l = list(map(int,input("enter values").split(" ")))
# p=l
# res = []
# for i in range(len(l)-1):
#         l.remove(l[i])
#         res.append(l)
#         l = p
# print(res)
# def list_elems(N):
#     res = []
#     while N != 0:
#         res.append(N % 10)
#         N = N // 10
#     return res
#
#
# def sum_split_list(N):
#     res = []
#     l = list_elems(N)
#     sum_n = sum(l)
#     for i in l:
#         res.append(sum_n - i)
#     return " ".join(map(str, res[::-1]))
#
#
# print(sum_split_list(1234))

#
# def sum_split_list(l):
#     res = []
#     sum_n = sum(l)
#     for i in l:
#         res.append(sum_n - i)
#     return " ".join(map(str, res))
#
#
# if __name__ == '__main__':
#     n = int(input("enter number n: "))
#     l = [int(i) for i in input("enter values").split()]
#     if len(l) == n:
#         print(sum_split_list(l))
#     else:
# #         print(f"enter {n} no of elements check enter values once", l)
# #
# def BinaryDecimal(n):  # user-defined function
#     return int(n, 2)
# # take inputs
# num = input('Enter a binary number: ')
#
# # display result
# print('The decimal value is =', BinaryDecimal(num))


# Function to print binary number using recursion
# def convertToBinary(n):
#     if n > 1:
#         convertToBinary(n // 2)
#     print(n % 2, end='')
#
#
# # decimal number
# dec = 34
#
# convertToBinary(dec)
# print()

# n = int(input("enter decimal value"))
# # while n != 0:
# #     r = n % 2
# #     print(r, end="")
# #     n = n // 2
# print(int(n,2))

#
# def binary_to_decimal(n):
#     return int(n, 2)
#
#
# n = 27
# binary_to_decimal(n)


# def BinaryDecimal(n):  # user-defined function
#     return int(n, 2)
#
# # take inputs
# num = input('Enter a binary number: ')
#
# # display result
# print('The decimal value is =', BinaryDecimal(num))


# n = "1234"
# l = list(n)
# res = []
# for i in range(len(l)):
#         l.remove(l[i])
#         res.append(sum(list(map(int,l))))
#         l = list(n)
# print(" ".join(map(str,res)))
# max_elem = max([int("".join(elem)) for elem in res])
# print(max_elem)








hglfijjf
kwjiii

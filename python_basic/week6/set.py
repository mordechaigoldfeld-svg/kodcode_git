# exe1

# num_lst=[1,2,2,3,1,4,3]
#
# def remove_duplicates(lis):
#     num_set=set(lis)
#     return  list(num_set)
#
# print(remove_duplicates(num_lst))



# exe2

# test_list=[1, 2, 2, 3, 1, 4]
#
# def len_set(lis):
#     set_list=set(lis)
#     cnt=0
#     for i in list(set_list):
#         cnt+=1
#     return cnt
#
# print(len_set(test_list))



# exe3
#
# ls1=[1, 2, 3, 4]
# ls2= [3, 4, 5, 6]
# def common_elements(l1,l2):
#     set1=set(ls1) & set(ls2)
#     ls3=[]
#     for i in set1:
#         if i in l1 and i in l2:
#             ls3.append(i)
#     return ls3
#
#
# print(common_elements(ls1,ls2))



# exe4

# ls1=[1, 2, 3, 4]
# ls2= [3, 4, 5, 6]
#
# def only_one(l1,l2):
#     l3=[]
#     set1=set(l1)
#     set2=set(l2)
#     set3=set1-set2 |set2-set1
#     for i in set3:
#         l3.append(i)
#     return l3
#
# print(only_one(ls1,ls2))



# exe5

# l1=[1,2,3]
# l2=[1,2,3,4,5]
# l3=[1,2,6]
# l4=[1,2,3,4,5]
#
# def is_subset(lis1,lis2):
#     ls5=[]
#     s1=set(lis2)
#     for i in s1:
#         if i in lis1:
#             ls5.append(i)
#     if len(ls5)==len(lis1):
#         return True
#     else:
#         return False
#
# print(is_subset(l1,l2))



# exe6
#
# def unique_char(stri):
#     s1=set(stri)
#     if len(s1)==len(stri):
#         return True
#     else:
#         return False
#
# print(unique_char('hello'))
# print(unique_char('helo'))




# exe7

# l1= [1, 2, 3, 2, 4, 1]
# l2=[1, 2, 3, 4]
#
# def first_repeated(lis):
#     s1=set()
#     for i in lis:
#         if i in s1:
#            return i
#         s1.add(i)
#
#
# print(first_repeated(l1))



# exe8

# s="The cat and the dog and the bird"
#
# def distinct_word(stri):
#     return len(set(stri.lower().split()))
#
#
# print(distinct_word(s))



# exe9

# l1=[3,1,4,7,2]
#
# def pair_sum_exist(lis,target):
#     s1=set()
#     for item in lis:
#         if target-item in s1:
#             return True
#         else:
#             s1.add(item)
#     return False
#
# print(pair_sum_exist(l1,6))





# exe10

# lis1=[1,2,3,4]
# lis2=[3,4,5,6]
#
# def symmetric_diference(l1,l2):
#     s1=set(l1)
#     s2=set(l2)
#     s3=(s1-s2)|(s2-s1)
#     return sorted(list(s3))
#
#
# print(symmetric_diference(lis1,lis2))



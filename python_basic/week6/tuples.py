# exe1

# tup_nums=(1,2,3,4,5)
#
# def sum_of_tuple(tup):
#     sum=0
#     for num in tup:
#         sum+=num
#     return sum
#
# print(sum_of_tuple(tup_nums))



# exe2


# tup_num=(3, 7, 2, 8, 5)
# def maximum_element(tup):
#     max=0
#     for num in tup:
#         if num > max:
#             max=num
#     return max
# print(maximum_element(tup_num))



# exe3

# tup_num=(2,4,2,3,2,1)
# def count_ocurrences(tup,value):
#     cnt=0
#     for i in tup:
#         if i == value:
#             cnt+=1
#     return cnt
#
#
# print(count_ocurrences(tup_num,2))



# exe4

# num_tup=(1,2,3,4)
# def reverse_tuple(tup):
#     num_list=list(tup)
#     new_lst=[]
#     for i in range(len(num_list)):
#         num = num_list.pop()
#         new_lst.append(num)
#     return tuple(new_lst)
#
#
# print(reverse_tuple(num_tup))
#


# exe5

# num_tup=(1,2,3,4,5,6,7,8)
#
# def swap_pairs(tup):
#     new_list=[]
#     if len(tup)%2 !=0:
#         return 'error'
#     else:
#         for i in tup[::2]:
#             new_list.append(i+1)
#             new_list.append(i)
#     return tuple(new_list)
#
# print(swap_pairs(num_tup))
#




# exe6

# num_tup=(4, 1, 7, 3, 5)
#
# def min_max(tup):
#     max=0
#     min=tup[0]
#     for i in tup:
#         if i> max:
#             max=i
#         elif i<min:
#             min=i
#     return min,max
#
# print(min_max(num_tup))



# exe7

# n1=(0,0)
# n2=(3,4)
#
#
# def distance_between_points(tup1,tup2):
#     x1,y1=tup1
#     x2,y2=tup2
#     distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
#     return distance
#
#
# print(distance_between_points(n1,n2))




# exe8

# t1=(3,1,4)
# t2=(1,5,9)
#
# def merge_sort(tup1,tup2):
#     lst1=list(tup1)+list(tup2)
#     lst1.sort()
#     return tuple(lst1)
#
# print(merge_sort(t1,t2))


# exe9

# letter_tup=('a','b','a','c','b','a')
#
# def frequency_table(tup):
#     n_lst=[]
#     letter_list=[]
#     for letter in tup:
#         if letter not in letter_list:
#             letter_list.append(letter)
#             n_lst.append( (letter,tup.count(letter)))
#
#     return tuple(n_lst)
#
# print(frequency_table(letter_tup))




# exe10

# tup_num=(1,2,3,4,5)
#
# def rotate_tuple(tup,k):
#     k= k% len(tup)
#     return tup[-k::]+tup[:-k:]
#
#
#
# print(rotate_tuple(tup_num,2))


t = (1, 2, 3)
t = t + (t[0],)
print(t)

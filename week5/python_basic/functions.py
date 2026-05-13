# x = 10
# def outer():
#     x = 20
#     def inner():
#         print(x)
#     inner()
# outer()
# print(x)


# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# c = make_counter()
# print(c())
# print(c())
# print(c())



# exe1
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# d=is_even(6)
# print(d)



# exe2

# def factorial(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *= i
#     return factorial
# f=factorial(5)
# print(f)




# exe3





# exe4

# def polindrome(word):
#     r=-1
#     for letter in word:
#         if letter == word[r]:
#             r -= 1
#         else:
#             return 'not palindrome'
#             break
#     else:
#         return 'palindrome'
# m=polindrome('helleh')
# n=polindrome('helomleh')
# print(m)
# print(n)



# exe5





# exe6

#
# def len_number(num):
#     len = 0
#     while num > 0:
#         len += 1
#         num = num // 10
#     return len
#
# a=len_number(10)
# print(a)

# exe7

# def reverse(num):
#     new=''
#     number=str(num)
#     for n in number:
#         if n =='0':
#             continue
#         else:
#             new+=n
#     return new[::-1]
#
# print(reverse(1200))
# print(reverse(675890))
#
#

# exe8
# def zero_end(arr):
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr.append(0)
#             arr.pop(i)
#     return arr
#
#
# c=zero_end([1,2,3,0,4,0,5])
# print(c)



# exe9

python_numbers = [4,7,2,9,1,5]
# python_numbers = [4,7,9]"צריך לתקן במידה והמספר הראשון הוא הקטן ביותר"
#
#
# def total_of_list(numbers):
#     sum = 0
#     max=0
#     min=0
#     for n in numbers:
#         sum += n
#         if n > max:
#             max = n
#         else:
#              if min ==0:
#                 min = n
#              elif n < min:
#                 min =n
#     average=sum/len(numbers)
#
#
#
#     return f' the sum of the list is: {sum} the average is: {average} the max is: {max} the min is: {min}'
#
# print(total_of_list(python_numbers))




# exe10

# list=[1,2,3,4,5]
# def reverse(list):
#   new_list=[]
#   for i in range(len(list)-1,-1,-1):
#     new_list.append(list[i])
#   return new_list
# print(reverse(list))



# exe11

list=[3,1,4,1,5,9,2,6,5,3]
def repeat(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(repeat(list))


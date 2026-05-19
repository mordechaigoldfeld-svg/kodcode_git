# exe1

#
# def safe_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None
#
# print(safe_int("12a"))
# print(safe_int("123"))



# exe2

# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return 'undefined'
#
#
# print(safe_divide(8,4))
# print(safe_divide(3,0))
#





# exe3

# def get_value(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return 'missing'
#
#
# print(get_value({'a':1}, 'a'))
# print(get_value({'a':1}, 'b'))







# exe4

# def parse_ints(values):
#     int_list = []
#     for val in values:
#         try:
#             int_list.append(int(val))
#         except ValueError:
#             pass
#     return int_list
#
#
# print(parse_ints(['1','2','x','3','y',7]))






# exe5

#
# def set_age(age):
#     try:
#         if age >=0 and age<=150:
#             return age
#         else:
#             raise ValueError('invalid age')
#     except:
#         raise ValueError('invalid age')
#
#
#
#
# print(set_age(25))
# print(set_age(-4))
# print(set_age(160))
# print(set_age(130))



# exe6

# def retry(func,n):
#     for i in range(n):
#         try:
#             return func()
#         except Exception:
#             if i == n-1:
#                 raise
#             print(f'round{i+1}')
#
#
#
# def say_hello():
#     print('hello')
#

# print(retry(say_hello(),3))
# print(retry(say_hello,3))














# exe1

# dic_test= {"a": 1, "b": 2, "c": 3}
#
# def sum_of_values(dic):
#     sum=0
#     for v in dic.values():
#         sum+=v
#     return sum
#
# print(sum_of_values(dic_test))





# exe2

# dic_test= {"a": 3, "b": 7, "c": 5}
#
# def key_with_max_value(dic):
#     max=0
#     name=''
#     for k,v in dic.items():
#         if v>max:
#             max=v
#             name=k
#
#     return  name
#
# print(key_with_max_value(dic_test))



# exe3


# def count_chareters(word:str):
#     word_dict={}
#     for letter in word:
#         if letter in word_dict:
#             word_dict[letter]+=1
#         else:
#             word_dict[letter]=1
#     return word_dict
#
# print(count_chareters('banana'))




# exe4

# test_dict={"a": 1, "b": 2, "c": 3}



# def invert_dict(dic):
#     new_dict={}
#     for k,v in dic.items():
#         new_dict[v]=k
#     return new_dict
#
# print(invert_dict(test_dict))


# exe5
#
# d1={"a": 1, "b": 2}
# d2={"b": 20, "c": 30}
#
#
# def merge_dict(dic1,dic2):
#     for key,value in dic2.items():
#         dic1[key]=value
#
#     return dic1
#
# print(merge_dict(d1,d2))




# exe6

# test_dict={"a": 1, "b": 5, "c": 3, "d": 8}
#
# def filter_by_value(dic,limit):
#     new_dict={}
#     for key,value in dic.items():
#         if value>limit:
#             new_dict[key]=value
#     return new_dict
#
#
# print(filter_by_value(test_dict,3))



# exe7

# test_list=["apple", "ant", "banana", "berry", "cherry"]
#
# def first_letter(word_list):
#     letter_dict={}
#     for word in word_list:
#         if word[0] in letter_dict:
#             letter_dict[word[0]]+=[word]
#         else:
#             letter_dict[word[0]]=[word]
#     return letter_dict
#
#
# print(first_letter(test_list))




# exe8

# word="the cat sat on the mat"
#
# def word_frequency(string):
#     string_dict={}
#     sp=string.split()
#     for i in sp:
#         if i in string_dict:
#             string_dict[i]+=1
#         else:
#             string_dict[i]=1
#     return string_dict
#
# print(word_frequency(word))





# exe9

# dict1={"a": 1, "b": 2, "c": 3}
# dict2={"b": 9, "c": 8, "d": 7}
#
# def common_keys(dic1,dic2):
#     common_list=[]
#     for key in dic1.keys():
#         if key in dic2:
#             common_list.append(key)
#     common_list.sort()
#     return common_list
#
#
# print(common_keys(dict1,dict2))





# exe10

# test_dict={"a": 1, "b": 2, "c": 2, "d": 3, "e": 2}
#
# def most_frequent_value(dic):
#     max=0
#     name=''
#     num_dict={}
#     for value in dic.values():
#         if value in num_dict:
#             num_dict[value]+=1
#         else:
#             num_dict[value]=1
#     print(num_dict)
#     for key,value in num_dict.items():
#         if value >max:
#             max=value
#             name=key
#     return name
#
#
# print(most_frequent_value(test_dict))






















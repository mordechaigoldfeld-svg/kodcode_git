# exe1


# for i in range(1,10):
#     if i % 2 == 0:
#         continue
#     elif i == 7:
#         break
#     else:
#         print(i)


# exe2

# while True:
#  password=input("Enter your password: ")
#  if password == "1234":
#      print("Welcome To Password Locker")
#      break
#  else:
#      print("try again")



# exe3

# list=[]
# product=input("enter the product")
# while product!="done":
#     list.append(product)
#     product=input("enter the product")
# print(list)



# exe3.2
# for i in range(4):
#     for j in range(3):
#         if i==2:
#             break
#         print(i,j)


# exe4
# vowel=0
# lower=0
# upper=0
# user=input("Enter a string: ")
# for letter in user:
#     if letter in "AEIOU":
#         upper+=1
#         vowel+=1
#     elif letter in "aeiou":
#         lower+=1
#         vowel +=1
#     else:
#         continue
# print(f'there are {vowel} vowels and {upper} uppercase and {lower} lowercase')
#


# exe5
# for i in range(1,6):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i * j}')




# exe6

# user=input("Enter your name: ")
# index=-1
# for letter in range(len(user)):
#     print(user[index])
#     index-=1


# exe7

# num='38261425'
# cnt=0
# even=0
# odd=0
# while cnt<(len(num)):
#     if int(num[cnt])%2==0:
#         even+=1
#     else:
#         odd+=1
#     cnt+=1
# print(f'there are {even} evens and {odd} odds')







# exe8
# name='moty'
# for letter in name:
#     print(letter*2,end='')


# exe9
# highest=0
# user=3
# while user!=0:
#     user = int(input("Enter a number: "))
#     if user>highest:
#         highest=user
# print(highest)



# exe10
#
# word='mordechai @ 34'
# for letter in word:
#    if letter not in 'abcdefghijklmnopqrstuvwxyz1234567890':
#        flag=True
#        break
#    else:
#        flag=False
# print(flag)



# exe11
# num=123
# new_num=0
#
# while num > 0:
#     last_digit=num%10
#     new_num=(new_num*10)+last_digit
#     num=num//10
# print(new_num)
#





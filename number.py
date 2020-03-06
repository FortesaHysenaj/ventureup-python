# def sum(a,b):
#     return a+b

#     print(sum(100,50))


# def greet(name):
#     print("hello"+name)


#     x=greet("Fortesa")
#     y=x
#     x="Aaaa"
#     print(x)
#     print(y)

# def solution(list_of_nums):
#     dic = dict()
#     count_even,count_odd = 0, 0
#     for i in list_of_nums:
#         if i % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     dic['ODD'] = count_odd
#     dic['EVEN'] = count_even
#     return dic

# l = [1, 2, 3, 5, 8, 9]
# print(solution(l))



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c=[]

# if len(b) < len(a):
#     for i in b:
#         if i in a and i not in c:
#             c.append(i)
         
# if len(b) > len(a):
#     for i in a:
#         if i in b and i not in c:
#             c.append(i)
                     
# print(c)

# set_a = set(a)
# set_b = set(b)

# common_list = list(set_a.intersection(set_b))

# print(common_list)


#1
lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))

while(lower_limit < upper_limit + 1):
    if(lower_limit % 2 != 0):
        print(lower_limit)
    lower_limit += 1
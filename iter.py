# class InfiniteNumber:
#     def __init__(self, starting_num):
#         self.starting_num = starting_num

#     def __iter__(self): 
#         return self
#         'American Ninja Warrior XP'
#     def __next__(self): # returns the next item in the sequence
#         self.starting_num = self.starting_num + 1
#         return self.starting_num

# # x = InfiniteNumber(5)

# # print(x.starting_num)
# # for i in x:
# #     print(i)

# # test_list = [1, 2, 3, 4]
# # # print(test_list)
# # to_iterate = iter(test_list)
# # print(to_iterate)
# # x = next(to_iterate)
# # y = next(to_iterate)
# # z = next(to_iterate)
# # print(x)
# # print(y)
# # print(z)


# word = '1234wo'
# def goes_after_og(word:str, first:str, second:str):
#     res = False
#     word = iter(word)
#     cur = next(word)
#     print(f'Starting letter is {cur} (cur)')
#     while cur != first:
#         cur = next(word)
#         print(f'Cur did not equal first! Cur is now {cur}')

#     cur = next(word)
#     if cur == second:
#         res = True

#     return res

# # print(goes_after(word, 'w', 'o'))

# def goes_after_v1(word:str, first:str, second:str):
#     res = False
#     for i in range(len(word)):
#         cur_letter = word[i]
#         if cur_letter == first:
#             next_letter = word[i + 1]
#             if next_letter == second:
#                 res = True
#     return res
# print(goes_after_v1('world', 'w', 'o'))

    
# 'sicko mode or mo bamba why not both'
# # pimp my ride pimp my horse





'Find Bonnie and Clyde'
'''
Given a list of names, find if the names Bonnie and Clyde are in this list, if they are then find out if they're next to each other
'''

names_list_1 = [
    'Aroosh',
    'Wesley',
    'Joe',
    'Donald',
    'Trump',
    'Bonnie',
    'Cliff',
    'Clyde'
]

names_list_2 = [
    'Cliff',
    'Aroosh',
    'Wesley',
    'Joe',
    'Donald',
    'Trump',
    'Bonnie',
    'Clyde'
]
names_list_3 = [
    'Cliff',
    'Aroosh',
    'Wesley',
    'Joe',
    'Donald',
    'Trump',
    'Clyde',
    'Bonnie',
]
def find_bc(names:list):
    # names = iter(names)
    # current = next(names)
    res = False
    for i in range(len(names)):
        if names[i] == 'Bonnie':
            res = names[i + 1] == 'Clyde'
            break
        elif names[i] == 'Clyde':
            res = names[i + 1] == 'Bonnie'
            break
    return res
# print(find_bc(names_list_1))
# print(find_bc(names_list_2))
# print(find_bc(names_list_3))


'''
Try using a while loop AND iter/next to iterate over lists that we would normally use a forloop for.
'''

num_list = [10, 5, 60, 7, 92, 32]
# For loop method
for num in num_list:
    print(num)

print('\n\n')

# iter/next method
iter_nums = iter(num_list)
cur = next(iter_nums)
while cur:
    print(cur)
    cur = next(iter_nums, None)




# import random
# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']

# p = 0
# m = 0
# k = 0
# l = 0
# d = 0

# for i in range(0, 100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p = p + 1 # p +=1 инкремент
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k += 1
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'dymdama':
#         d += 1

# # print(f'Plov: {p}, \nManty:{m}, \nKuurdak: {k}, \nLagman: {l} ')

# dict_ = {'Plov': p, 'Manty': m, 'Kuurdak': k, 'Lagman': l, 'Dymdama': d}
# #print(dict_)

# res = sorted(dict_.items(), key = lambda x: x[1])    
# winner = res[-1]
# print(f'победило блюдо {winner[0]}, оно набрало: {winner[1]}')

#Counting Valleys Haccerrank

def countingValleys(steps, path):
    dolina = 0
    sea_level = 0
    for x in path:
        if x == 'U':
            sea_level += 1
            if sea_level ==0:
                dolina += 1
        elif x == 'D':
            sea_level -=1
    return dolina
print(countingValleys(100,'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'))
















































#1. ls =[]
# for i in range(0, 200):
#     if i % 2 == 0:
#         print(i)
# print(ls)


#2. ls = []
# for i in range(0, 200):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
# print(ls)


# ls = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         ls.append(i**2)
#     else:
#         i % 2 != 0
#         ls.append(i)
# print(ls)
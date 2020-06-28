def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    new_list = list[1:]
    del new_list[-1]
    return new_list

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

print(chop(list1))
print(middle(list2))

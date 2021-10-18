# this code is about searching

"""
The Sequential Search
"""
def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        pos += 1

    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13,0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            break
        pos += 1

    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))


"""
The Binary Search
"""
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2 
        if a_list[middle] == item:
            found = True
        elif a_list[middle] > item:
            last = middle - 1
        else:
            first = middle + 1
    
    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))


def binary_search_recursion(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        middle = len(a_list) // 2

    if a_list[middle] == item:
        return True
    elif a_list[middle] > item:
        return binary_search(a_list[:middle], item)
    else:
        return binary_search_recursion(a_list[middle+1:], item)
    
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_recursion(test_list, 3))
print(binary_search_recursion(test_list, 13))




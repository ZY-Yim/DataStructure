# this file is about sorting

# bubble sort
def bubble_sort(a_list):
    for i in range(len(a_list)-1):
        for j in range(len(a_list)-1-i):
            if a_list[j] > a_list[j+1]:
                # tmp = a_list[j+1]
                # a_list[j+1] = a_list[j]
                # a_list[j] = tmp
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
    print(a_list)


# short bubble sort
def short_bubble_sort(a_list):
    exchange = True
    for i in range(len(a_list)-1):
        exchange = False
        for j in range(len(a_list)-1-i):
            if a_list[j] > a_list[j+1]:
                exchanges = True
                # tmp = a_list[j+1]
                # a_list[j+1] = a_list[j]
                # a_list[j] = tmp
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
        if not exchange:
            break
    print(a_list)


def selection_sort(a_list):
    for i in range(len(a_list)-1):
        max_pos = 0
        for j in range(1, len(a_list)-i):    
            if a_list[j] > a_list[max_pos]:
                max_pos = j
        a_list[len(a_list)-1-i], a_list[max_pos] = a_list[max_pos],  a_list[len(a_list)-1-i]
    print(a_list)


def insert_sort(a_list):
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        pos = i
        while pos > 0 and a_list[pos-1] > current_value:
            a_list[pos] = a_list[pos-1]
            pos -= 1
        a_list[pos] = current_value
    print(a_list)


def gap_insert_sort(a_list, start_pos, gap):
    for i in range(start_pos + gap, len(a_list), gap):
        current_value = a_list[i]
        pos = i
        while pos >= gap and a_list[pos-gap] > current_value:
            a_list[pos] = a_list[pos-gap]
            pos -= gap
        a_list[pos] = current_value


def shell_sort(a_list):
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for i in range(sublist_count):
            gap_insert_sort(a_list, i, sublist_count)

        print("the list after insert sorti of increment size ", sublist_count, "the list is ", a_list)
        sublist_count = sublist_count // 2
        

def merge_sort(a_list):
    print("spliting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        # merge
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    
    print("mergeing ", a_list)


def quickSort(a_list):
   quickSortHelper(a_list,0,len(a_list)-1)
   print(a_list)


def quickSortHelper(a_list,first,last):
   if first<last:
       splitpoint = partition(a_list,first,last)

       quickSortHelper(a_list,first,splitpoint-1)
       quickSortHelper(a_list,splitpoint+1,last)


def partition(a_list,first,last):
   pivotvalue = a_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and a_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while a_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = a_list[leftmark]
           a_list[leftmark] = a_list[rightmark]
           a_list[rightmark] = temp

   temp = a_list[first]
   a_list[first] = a_list[rightmark]
   a_list[rightmark] = temp

   return rightmark


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
short_bubble_sort(a_list)
selection_sort(a_list) 
insert_sort(a_list)
shell_sort(a_list)
merge_sort(a_list)
quickSort(a_list)


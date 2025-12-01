import random
import time


def increasing_comparator(a, b):
    return a > b


def decreasing_comparator(a, b):
    return a < b


def first_pivot(a_list):
    return 0


def mid_pivot(a_list):
    return len(a_list) // 2


def random_pivot(a_list):
    return random.randrange(len(a_list))


def random_list(length):
    # underscore is just vscodes way of understanding that the variable is not going to be used,
    # it is not functionally different from an unused variable name 'foo'

    #   return     a random integer      for every value in range of length
    return [random.randint(0, length) for foo in range(length)]


def swap(a_list, a, b):
    va = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = va


def shift(a_list, i, comparator=increasing_comparator):
    while i > 0:
        if comparator(a_list[i - 1], a_list[i]):
            swap(a_list, i - 1, i)
            i = i - 1

        else:
            i = i - 1
    return a_list


def insertion_sort(a_list, comparator=increasing_comparator):
    for i in range(len(a_list)):
        shift(a_list, i, comparator)

    return a_list


def time_functions(a_list, function, comparator=increasing_comparator):
    begin = time.perf_counter()
    function(a_list)
    end = time.perf_counter()
    return end - begin


def shift_wo_swap(a_list, i, comparator=increasing_comparator):
    # reduces number of operations performed
    # wo=without
    while i > 0:
        target = a_list[i]
        new = a_list[i - 1]
        if comparator(a_list[i - 1], target):
            a_list[i - 1] = target
            a_list[i] = new
            i -= 1

        else:
            i -= 1
    return a_list


def insertion_sort_wo_swap(a_list, comparator=increasing_comparator):
    for i in range(len(a_list)):
        shift_wo_swap(a_list, i, comparator)
    return a_list


def split(a_list):
    # compute midpoint
    mid = len(a_list) // 2
    count = 0
    a = []
    b = []
    # slice list

    count += 1
    left = a_list[:mid]
    right = a_list[mid:]
    return left, right

    # return both halves


def merge(left, right):
    # let li = 0 and ri = 0
    li = 0
    ri = 0
    merged = []
    # while li <len(left_ and ri <right len
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            merged.append(left[li])
            li += 1
        # if  the value at li is less than the bealue ar ri
        # append li to merged list
        # increment li
        # else
        else:
            merged.append(right[ri])
            ri += 1
    if li < len(left):
        merged += left[li:]
    else:
        merged += right[ri:]
    # append ri to merged list
    # increment ri
    return merged


def merge_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        left, right = split(a_list)

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        merged = merge(sorted_left, sorted_right)
        return merged


def bubble_sort(a_list, comparator=increasing_comparator):
    count = 0
    while count < len(a_list):
        for i in range(len(a_list) - 1):
            if comparator(a_list[i], a_list[i + 1]):
                swap(a_list, i, i + 1)
        count += 1
    return a_list


def partition(pivot, a_list):
    less = []
    equal = []
    greater = []
    for i in a_list:
        if i < pivot:
            less.append(i)
        if i == pivot:
            equal.append(i)
        if i > pivot:
            greater.append(i)
    return less, equal, greater


def quicksort(a_list, pivot_func=first_pivot):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[pivot_func(a_list)]
        less, eq, greater = partition(pivot, a_list)
        sorted_less = quicksort(less, pivot_func)
        sorted_greater = quicksort(greater, pivot_func)

        return sorted_less + eq + sorted_greater

def quick_insertion_sort(a_list, pivot_func=first_pivot,count=0):
    if len(a_list) < 2:
        return a_list
    else:
        count +=1
        if count<950:
            pivot = a_list[pivot_func(a_list)]
            less, eq, greater = partition(pivot, a_list)
            sorted_less = quick_insertion_sort(less, pivot_func,count)
            sorted_greater = quick_insertion_sort(greater, pivot_func,count)
            a_list = sorted_less + eq + sorted_greater
        if count >=950:
            insertion_sort(a_list)

        return a_list

def quicksort_mid(a_list):
    return quicksort(a_list, mid_pivot)


def quicksort_random(a_list):
    return quicksort(a_list, random_pivot)


def main():
    a = list(range(1, 3001))
    copya = list(a)
    b = list(range(3001, 1, -1))
    copyb = list(b)
    c = random_list(3000)
    copyc = list(c)

    # print(a)
    # shift(a, 1)
    # print(a)
    # print(shift(a,4))
    # print(bubble_sort(a))

    print(
        "Insertion Sort Sorted:",
        time_functions(copya, insertion_sort, increasing_comparator),
    )
    print(
        "Insertion Sort Reverse",
        time_functions(copyb, insertion_sort, increasing_comparator),
    )
    print(
        "Insertion Sort Random",
        time_functions(copyc, insertion_sort, increasing_comparator),
    )

    copya = list(a)
    copyb = list(b)
    copyc = list(c)

    print(
        "Inserton Sort Sorted W/O Swap:",
        time_functions(copya, insertion_sort_wo_swap, increasing_comparator),
    )
    print(
        "Insertion Sort Reverse W/O Swap",
        time_functions(copyb, insertion_sort_wo_swap, increasing_comparator),
    )
    print(
        "Insertion Sort Random W/O Swap",
        time_functions(copyc, insertion_sort_wo_swap, increasing_comparator),
    )

    copya = list(a)
    copyb = list(b)
    copyc = list(c)

    print(
        "Bubble Sort Sorted", time_functions(copya, bubble_sort, increasing_comparator)
    )
    print(
        "Bubble Sort Reverse", time_functions(copyb, bubble_sort, increasing_comparator)
    )
    print(
        "Bubble Sort Random", time_functions(copyc, bubble_sort, increasing_comparator)
    )

    copya = list(a)
    copyb = list(b)
    copyc = list(c)

    print("Quicksort Sorted", time_functions(copya, quick_insertion_sort, increasing_comparator))
    # print("Quicksort Reverse", time_functions(copyb, quicksort, increasing_comparator))
    print("Quicksort Random", time_functions(copyc, quick_insertion_sort, increasing_comparator))
    # c = list((range(4999,-1,-1)))
    # # print("random", time_insertion_sort(c))
    # lst = [6, 4, 5, 3, 2]
    # print(lst)
    # i = 3
    # # invoke
    # actual = ishift(lst, i, decreasing_comparator)
    # print(actual)


if __name__ == "__main__":
    main()


# 10,3,5,6,1,4,8,7
# 3,5,6,1,4,8,7[10]
# [1][3][5,6,4,8,7][10]
# [1][3][4][5][6,8,7][10]
# [1][3][4][5][6][7][8][10]
# [1,2,4,5,6,7,8,10]

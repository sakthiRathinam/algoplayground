import typing

def insertion_sort(lst:typing.List,ascending:bool=True) -> typing.List:
    for i in range(1,len(lst)):
        current = lst[i]
        while True:
            ascending_check =  i > 0 and lst[i-1] > current and ascending
            descending_check = i > 0 and lst[i-1] < current and not ascending
            if not ascending_check and not descending_check:
                break
            lst[i] = lst[i-1]
            i = i - 1
            lst[i] = current

    return lst


print(insertion_sort([4,2,5,7,3,1]))


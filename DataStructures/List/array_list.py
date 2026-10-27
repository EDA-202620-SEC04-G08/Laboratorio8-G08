from heapq import merge
from operator import index
from typing_extensions import final


def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist


def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    return my_list["elements"][pos]


def is_present(my_list, element, cmp_function):
    size = my_list["size"]

    if size > 0:
        keyexist = False

        for keypos in range(0, size):
            info = my_list["elements"][keypos]

            if cmp_function(element, info) == 0:
                keyexist = True
                break

        if keyexist:
            return keypos

    return -1



def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")

    return my_list["elements"][0]


def is_empty(my_list):
    return my_list["size"] == 0


def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")

    return my_list["elements"][my_list["size"] - 1]


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    del my_list["elements"][pos]
    my_list["size"] -= 1

    return my_list


def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")

    removed_element = my_list["elements"].pop(0)
    my_list["size"] -= 1

    return removed_element


def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")

    removed_element = my_list["elements"].pop()
    my_list["size"] -= 1

    return removed_element


def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")

    my_list["elements"].insert(pos, element)
    my_list["size"] += 1

    return my_list


def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    my_list["elements"][pos] = new_info

    return my_list


def exchange(my_list, pos_1, pos_2):
    if (
        pos_1 < 0
        or pos_1 >= my_list["size"]
        or pos_2 < 0
        or pos_2 >= my_list["size"]
    ):
        raise IndexError("list index out of range")

    my_list["elements"][pos_1], my_list["elements"][pos_2] = (
        my_list["elements"][pos_2],
        my_list["elements"][pos_1]
    )

    return my_list


def sub_list(my_list, pos_i, num_elements):
    if (
        pos_i < 0
        or num_elements < 0
        or pos_i >= my_list["size"]
        or pos_i + num_elements > my_list["size"]
    ):
        raise IndexError("list index out of range")

    result = new_list()

    for pos in range(pos_i, pos_i + num_elements):
        add_last(result, my_list["elements"][pos])

    return result


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if float(element_1) < float(element_2):
        is_sorted = True
    return is_sorted


def selection_sort(my_list, sort_crit):
    tamano_lista = size(my_list)
    for i in range(tamano_lista):
        mas_pequeno = i
        for j in range(i+1,tamano_lista):
            elemento1 = get_element(my_list, mas_pequeno)
            elemento2 = get_element(my_list,j)
            if sort_crit(elemento1, elemento2) == False:
                mas_pequeno = j
                
        if mas_pequeno != i:
            exchange(my_list, i,mas_pequeno)
    return my_list
            
                
        
def insertion_sort(my_list, sort_crit):
    n = my_list["size"]
    for i in range(1, n):
        j = i   
        while j > 0 and sort_crit(my_list["elements"][i], my_list["elements"][j-1]):
            exchange (my_list, j, j - 1)
            j -= 1
    return my_list

def shell_sort(my_list, sort_crit):
    sz = size(my_list)
    gap = sz // 2
    while gap > 0:
        for i in range(gap, sz):
            temp = get_element(my_list, i)
            j = i

            while j >= gap and sort_crit(get_element(my_list, j - gap), temp):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2

def merge(list1, list2, sort_crit):
    result = new_list()
    i = 0
    j = 0

    while i < size(list1) and j < size(list2):
        if sort_crit(get_element(list1, i), get_element(list2, j)):
            add_last(result, get_element(list1, i))
            i += 1
        else:
            add_last(result, get_element(list2, j))
            j += 1

    while i < size(list1):
        add_last(result, get_element(list1, i))
        i += 1

    while j < size(list2):
        add_last(result, get_element(list2, j))
        j += 1

    return result

def merge_sort(my_list, sort_crit):

    if size(my_list) <= 1:
        return my_list
    else:
        mitad = size(my_list) // 2
        izq = sub_list(my_list, 0, mitad)
        der = sub_list(my_list, mitad, size(my_list) - mitad)

        izq_ord = merge_sort(izq, sort_crit)
        der_ord = merge_sort(der, sort_crit)

        return merge(izq_ord, der_ord, sort_crit)
    
def quick_sort(my_list, sort_crit): 
    if size(my_list) <= 1:
        return my_list
    else:
        pivote = get_element(my_list, 0)
        menores = new_list()
        mayores = new_list()

        for i in range (1, size(my_list)):
            elemento = get_element(my_list, i)
            if sort_crit(elemento, pivote):
                add_last(menores, elemento)
            else:
                add_last(mayores, elemento)

        menores_ord = quick_sort(menores, sort_crit)
        mayores_ord = quick_sort(mayores, sort_crit)

        result = new_list()
        for i in range(size(menores_ord)):
            add_last(result, get_element(menores_ord, i))
        add_last(result, pivote)
        for i in range(size(mayores_ord)):
            add_last(result, get_element(mayores_ord, i))

        return result


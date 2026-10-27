import DataStructures.List.list_node as ln

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cnp_function):
    is_in_array = False
    temp = my_list["first"]
    count =0
    while not is_in_array and temp is not None:
        if cnp_function(element ,temp["info"] ) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        return count - 1
    return count


def add_first(my_list, element):
    nuevo_nodo = {"info": element,
                "next": my_list["first"]
                }
    my_list["first"] = nuevo_nodo
    if my_list["size"] == 0:
        my_list["last"] = nuevo_nodo
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    nuevo_nodo = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = nuevo_nodo
    else:
        my_list["last"]["next"] = nuevo_nodo
    my_list["last"] = nuevo_nodo
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["first"] is not None:
        return my_list["first"]["info"]
    return None


def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False


def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]


def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    elif my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        prev = my_list["first"]
        
        while searchpos <pos:
            prev = node
            node = node["next"]
            searchpos += 1
        prev["next"] = node["next"]
        my_list["size"] -=1

    
    return my_list


def remove_first(my_list):

    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    node = my_list["first"]

    if my_list["size"] > 0:
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
            my_list["size"] = 0

        else:
            my_list["first"]=node["next"]
            my_list["size"] -= 1
    return node["info"]


def remove_last(my_list):

    if is_empty(my_list):
            raise Exception('IndexError: list index out of range')

    last = my_list["last"]

    if my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        
        while searchpos < my_list["size"]-2:
            node = node["next"]
            searchpos += 1
            
        node["next"] = None
        my_list["last"]=node
        my_list["size"]-=1
    return last["info"]


def insert_element(my_list, element, pos):

    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    newnode = ln.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["last"] = newnode
        my_list["first"] = newnode
        my_list["size"]+=1

    elif my_list["size"] > 0:

        searchpos = 0
        node = my_list["first"]
        prev = my_list["first"]
        
        while searchpos <=pos:
            prev = node
            node = node["next"]
            searchpos += 1
        newnode["next"] = node
        prev["next"] = newnode
        my_list["size"] +=1
    
    return my_list


def change_info(my_list, pos, new_info):

    if pos < 0 or pos > size(my_list):
            raise Exception('IndexError: list index out of range')

    elif my_list["size"] == 0:
        if pos == 0:
            newnode = ln.new_single_node(new_info)    
            my_list["first"] = newnode
            my_list["last"] = newnode
            my_list["size"] = 1
    elif my_list["size"] > 0:
        searchpos = 0
        node = my_list["first"]
        
        while searchpos < pos:
            
            node = node["next"]
            searchpos += 1
        node["info"] = new_info
    
    return my_list


def exchange(my_list, pos1, pos2):

    if pos1 < 0 or pos1 > size(my_list) or pos2 < 0 or pos2 > size(my_list):
            raise Exception('IndexError: list index out of range')

    elif my_list["size"] > 0:

        el1=get_element(my_list, pos1)
        el2=get_element(my_list, pos2)
        change_info(my_list, pos1, el2)
        change_info(my_list, pos2, el1)
    return my_list


def sub_list(my_list, pos, num_elements):
    sublist = new_list()
    if pos<0 or pos>=my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    elif my_list["size"] > 0:
        searchpos=0
        node = my_list["first"]

        while searchpos < pos:
            node = node["next"]
            searchpos += 1

        sublist["first"] = node
        searchpos=0
        node = sublist["first"]

        while searchpos < num_elements:
            node = node["next"]
            searchpos += 1
        node["next"] = None
        sublist["last"] = node
        sublist["size"] = num_elements
    
    return sublist
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if float(element_1) < float(element_2):
        is_sorted = True
    return is_sorted

def insertion_sort(my_list, sort_crit):
    n = my_list["size"]
    for i in range(1, n):
        j = i
        while j > 0 and sort_crit(get_element(my_list, i), get_element(my_list, j)):
            exchange(my_list, j, j - 1)
            j -= 1

    return my_list

def selection_sort(my_list, sort_crit):
    nodo = my_list["first"]
    while nodo is not None:
        nodo_mas_pequeno = nodo
        nodo_siguiente = nodo["next"]
        while nodo_siguiente is not None:
            elemento1 = nodo_mas_pequeno["info"]
            elemento2 = nodo_siguiente["info"]
            if sort_crit(elemento1, elemento2) == False:
                nodo_mas_pequeno = nodo_siguiente
            nodo_siguiente = nodo_siguiente["next"]
        if nodo_mas_pequeno != nodo:
            intercambio = nodo["info"]
            nodo["info"] = nodo_mas_pequeno["info"]
            nodo_mas_pequeno["info"] = intercambio
        nodo = nodo["next"]
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
    nodo1 = list1["first"]
    nodo2 = list2["first"]
    while nodo1 is not None and nodo2 is not None:
        if sort_crit(nodo1["info"], nodo2["info"]):
            add_last(result, nodo1["info"])
            nodo1=nodo1["next"]
        else:
            add_last(result, nodo2["info"])
            nodo2 = nodo2["next"]

    while nodo1 is not None:
        add_last(result, nodo1["info"])
        nodo1 = nodo1["next"]

    while nodo2 is not None:
        add_last(result, nodo2["info"])
        nodo2 = nodo2["next"]
    return result

def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    else:
        mitad = size(my_list) // 2
        izq = new_list()
        der = new_list()
        for i in range(mitad):
            add_last(izq, get_element(my_list, i))
        for j in range(mitad, size(my_list)):
            add_last(der, get_element(my_list, j))

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
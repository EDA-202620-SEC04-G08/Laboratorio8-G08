from DataStructures.Tree import bst_node as node
from DataStructures.List import single_linked_list as sl

def new_map():
    arbol = {"root":None}
    return arbol

def size_tree(root):
    if root is None:
        tamano = 0
    else:
        tamano = root["size"]
    return tamano

def insert_node (root, key, value):
    if root is None:
        return node.new_node(key,value)
    if key == node.get_key(root):
        root["value"] = value
    elif key < root["key"]:
        root["left"] = insert_node(root["left"],key,value)
    else:
        root["right"] = insert_node(root["right"],key,value)
    
    root["size"] = 1 + size_tree(root["left"])+ size_tree(root["right"])
    return root
    
def put (my_bst, key, value):
    if my_bst is None:
        my_bst = new_map(None)
    if my_bst["root"] is None:
        my_bst["root"] = node.new_node(key,value)
    else:
        insert_node(my_bst["root"],key,value)
    return my_bst

def get_node(root,key):
    if root is None:
        valor = None
    else:
        llave = node.get_key(root) 
        if llave == key:
            valor = node.get_value(root)
        elif key < llave:
            valor = get_node(root["left"],key)
        else:
            valor = get_node(root["right"],key)
    return valor
    
def get (my_bst, key):
    if my_bst is None or my_bst["root"] is None:
        valor = None
    else:
        valor = get_node(my_bst["root"],key)
    return valor

def size(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return 0
    else:
        return size_tree(my_bst["root"])

def contains (my_bst,key):
    valor = False
    if get(my_bst,key) is not None:
        valor = True
    return valor

def is_empty (my_bst):
    valor = False
    if my_bst is None or my_bst["root"] is None:
        valor = True
    return valor

def get_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return node.get_key(root)
    
    return get_min_node(root["left"])

def get_min(my_bst):
    return get_min_node(my_bst["root"])

def get_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return node.get_key(root)
    
    return get_max_node(root["right"])

def get_max(my_bst):
    return get_max_node(my_bst["root"])

def delete_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        valor = root["right"]
    else:
        root["left"] = delete_min_node(root["left"])
        valor = root
    return valor

def delete_min(my_bst):
    if my_bst is None or my_bst["root"] is None:
        valor = None
    else:
        my_bst["root"] = delete_min_node(my_bst["root"])
        valor = my_bst
    return valor

def key_set_tree (root,key_list):
    if root is not None:
        key_set_tree(root["left"],key_list)
        llave = node.get_key(root)
        sl.add_last(key_list, llave)
        key_set_tree(root["right"],key_list)
    return key_list

def key_set(my_bst):
    lista_llaves = sl.new_list()
    if my_bst is not None:
        key_set_tree(my_bst["root"],lista_llaves)
    return lista_llaves

def value_set_tree (root,value_list):
    if root is not None:
        value_set_tree(root["left"],value_list)
        llave = node.get_key(root)
        sl.add_last(key_list, llave)
        value_set_tree(root["right"],value_list)
    return value_list

def value_set(my_bst):
    lista_valores = sl.new_list()
    if my_bst is not None:
        key_set_tree(my_bst["root"],lista_valores)
    return lista_valores

def delete_max_tree(root):
    if root is None:
        valor = None
    elif root["right"] is None:
        valor = root["left"]
    else:
        root["right"] = delete_max_tree(root["right"])
        valor = root
    return valor

def delete_max(my_bst):
    if my_bst is None or my_bst["root"] is None:
        valor = None
    else:
        my_bst["root"] = delete_max_tree(my_bst["root"])
        valor = my_bst
    return valor   

def height_tree(root):
    if root is None:
        valor = 0
    else:
        altura_izq = height_tree(root["left"])
        altura_der = height_tree(root["right"])
        valor = 1+max(altura_izq,altura_der)
    return valor

def height(my_bst):
    valor = height_tree(my_bst["root"])
    return valor

def keys_range(root, key_initial,key_final,list_key):
    if root is not None:
        llave = node.get_key(root)
        if key_initial<llave:
            keys_range(root["left"],key_initial,key_final,list_key)
        if llave >= key_initial and llave <= key_final:
            sl.add_last(list_key,llave)
        if llave < key_final:
            keys_range(root["right"],key_initial,key_final,list_key)
    return list_key

def keys(my_bst,key_initial,key_final):
    lista_llaves = sl.new_list()
    lista = keys_range(my_bst["root"],key_initial,key_final,lista_llaves)
    return lista

def values_range(root, key_initial,key_final,list_values):
    if root is not None:
        llave = node.get_key(root)
        if key_initial<llave:
            values_range(root["left"],key_initial,key_final,list_values)
        if llave >= key_initial and llave <= key_final:
            sl.add_last(list_values,root["value"])
        if llave < key_final:
            values_range(root["right"],key_initial,key_final,list_values)
    return list_values

def values(my_bst,key_initial,key_final):
    lista_values = sl.new_list()
    lista = values_range(my_bst["root"],key_initial,key_final,lista_values)
    return lista
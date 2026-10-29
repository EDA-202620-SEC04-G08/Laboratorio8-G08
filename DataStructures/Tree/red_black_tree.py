from DataStructures.Tree import rbt_node as rn
from DataStructures.List import single_linked_list as sl

def new_map():
    arbol = {"root": None}
    return arbol

def default_compare(key, element):
    k = rn.get_key(element)
    if key == k:
        return 0
    elif key > k:
        return 1
    return -1

def rotate_left(node_rbt):
    x = node_rbt["right"]
    node_rbt["right"] = x["left"]
    x["left"] = node_rbt
    rn.change_color(x, node_rbt["color"])
    rn.change_color(node_rbt, rn.RED)
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"])
    return x

def rotate_right(node_rbt):
    x = node_rbt["left"]
    node_rbt["left"] = x["right"]
    x["right"] = node_rbt
    rn.change_color(x, node_rbt["color"])
    rn.change_color(node_rbt, rn.RED)
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"])
    return x

def flip_node_color(node):
    if node is not None:
        if rn.is_red(node):
            rn.change_color(node,rn.BLACK)
        else:
            rn.change_color(node, rn.RED)
    return node

def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    return node_rbt

def size_tree(root):
    valor = 0
    if root is not None:
        valor = root["size"]
    return valor

def is_red(node):
    valor = False
    if node is not None:
        valor = rn.is_red(node) 
    return valor

def insert_node(root, key, value):
    if root is None:
        return rn.new_node(key, value)          

    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rn.change_color(my_rbt["root"], rn.BLACK)
    return my_rbt

def get_node(root,key):
    valor = None
    if root is not None:
        comparacion = default_compare(key,root)
        if comparacion < 0:
            valor = get_node(root["left"],key)
        elif comparacion >0:
            valor = get_node(root["right"],key)
        else:
            valor= rn.get_value(root)
    return valor

def get(my_rbt, key):
    if my_rbt is None or my_rbt["root"] is None:
        valor = None
    else:
        valor = get_node(my_rbt["root"],key)
    return valor

def contains(my_rbt, key):
    valor = get(my_rbt,key)
    verdadero = False
    if valor is not None:
        verdadero = True
    return verdadero

def size(my_rbt):
    tamano = 0
    if my_rbt is not None:
        tamano = size_tree(my_rbt["root"])
    return tamano

def is_empty(my_rbt):
    tamno = size(my_rbt)
    valor = False
    if tamno == 0:
        valor = True
    return valor

def key_set_tree(root,key_list):
    if root is not None:
        key_set_tree(root["left"],key_list)
        sl.add_last(key_list, rn.get_key(root))
        key_set_tree(root["right"],key_list)
    return key_list

def key_set(my_rbt):
    llaves = sl.new_list()
    if my_rbt is not None:
        key_set_tree(my_rbt["root"],llaves)
    return llaves

def value_set_tree(root,value_list):
    if root is not None:
        value_set_tree(root["left"],value_list)
        sl.add_last(value_list,rn.get_value(root))
        value_set_tree(root["right"],value_list)
    return value_list

def value_set(my_rbt):
    valores = sl.new_list()
    if my_rbt is not None:
        value_set_tree(my_rbt["root"],valores)
    return valores

# A partir de acá, las implementaciones fueron hechas por Juan José Peñaloza con ayuda de Claude Sonnet 5.5

def get_min_node(root):
    valor = None
    if root is not None:
        if root["left"] is None:
            valor = rn.get_key(root)
        else:
            valor = get_min_node(root["left"])
    return valor

def get_min(my_rbt):
    llave = None
    if my_rbt is not None:
        llave = get_min_node(my_rbt["root"])
    return llave

def get_max_node(root):
    valor = None
    if root is not None:
        if root["right"] is None:
            valor = rn.get_key(root)
        else:
            valor = get_max_node(root["right"])
    return valor

def get_max(my_rbt):
    llave = None
    if my_rbt is not None:
        llave = get_max_node(my_rbt["root"])
    return llave

# ---------- Balanceo y eliminación ----------

def balance(root):
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def move_red_left(root):
    flip_colors(root)
    if is_red(root["right"]["left"]):
        root["right"] = rotate_right(root["right"])
        root = rotate_left(root)
        flip_colors(root)
    return root

def move_red_right(root):
    flip_colors(root)
    if is_red(root["left"]["left"]):
        root = rotate_right(root)
        flip_colors(root)
    return root

def delete_min_node(root):
    if root["left"] is None:
        return None
    if not is_red(root["left"]) and not is_red(root["left"]["left"]):
        root = move_red_left(root)
    root["left"] = delete_min_node(root["left"])
    return balance(root)

def delete_min(my_rbt):
    if my_rbt is not None and my_rbt["root"] is not None:
        raiz = my_rbt["root"]
        if not is_red(raiz["left"]) and not is_red(raiz["right"]):
            rn.change_color(raiz, rn.RED)
        my_rbt["root"] = delete_min_node(raiz)
        if my_rbt["root"] is not None:
            rn.change_color(my_rbt["root"], rn.BLACK)
    return my_rbt

def delete_max_node(root):
    if is_red(root["left"]):
        root = rotate_right(root)
    if root["right"] is None:
        return None
    if not is_red(root["right"]) and not is_red(root["right"]["left"]):
        root = move_red_right(root)
    root["right"] = delete_max_node(root["right"])
    return balance(root)

def delete_max(my_rbt):
    if my_rbt is not None and my_rbt["root"] is not None:
        raiz = my_rbt["root"]
        if not is_red(raiz["left"]) and not is_red(raiz["right"]):
            rn.change_color(raiz, rn.RED)
        my_rbt["root"] = delete_max_node(raiz)
        if my_rbt["root"] is not None:
            rn.change_color(my_rbt["root"], rn.BLACK)
    return my_rbt


# ---------- Floor y ceiling ----------

def floor_key(root, key):
    valor = None
    if root is not None:
        comparacion = default_compare(key, root)
        if comparacion == 0:
            valor = rn.get_key(root)
        elif comparacion < 0:
            valor = floor_key(root["left"], key)
        else:
            candidato = floor_key(root["right"], key)
            if candidato is not None:
                valor = candidato
            else:
                valor = rn.get_key(root)
    return valor

def floor(my_rbt, key):
    valor = None
    if my_rbt is not None:
        valor = floor_key(my_rbt["root"], key)
    return valor

def ceiling_key(root, key):
    valor = None
    if root is not None:
        comparacion = default_compare(key, root)
        if comparacion == 0:
            valor = rn.get_key(root)
        elif comparacion > 0:
            valor = ceiling_key(root["right"], key)
        else:
            candidato = ceiling_key(root["left"], key)
            if candidato is not None:
                valor = candidato
            else:
                valor = rn.get_key(root)
    return valor

def ceiling(my_rbt, key):
    valor = None
    if my_rbt is not None:
        valor = ceiling_key(my_rbt["root"], key)
    return valor


# ---------- Select y rank (posición base 0) ----------

def select_key(root, pos):
    valor = None
    if root is not None:
        izq = size_tree(root["left"])
        if izq > pos:
            valor = select_key(root["left"], pos)
        elif izq < pos:
            valor = select_key(root["right"], pos - izq - 1)
        else:
            valor = rn.get_key(root)
    return valor

def select(my_rbt, pos):
    valor = None
    if my_rbt is not None and 0 <= pos < size(my_rbt):
        valor = select_key(my_rbt["root"], pos)
    return valor

def rank_keys(root, key):
    cantidad = 0
    if root is not None:
        comparacion = default_compare(key, root)
        if comparacion < 0:
            cantidad = rank_keys(root["left"], key)
        elif comparacion > 0:
            cantidad = 1 + size_tree(root["left"]) + rank_keys(root["right"], key)
        else:
            cantidad = size_tree(root["left"])
    return cantidad

def rank(my_rbt, key):
    cantidad = 0
    if my_rbt is not None:
        cantidad = rank_keys(my_rbt["root"], key)
    return cantidad


# ---------- Altura ----------

def height_tree(root):
    altura = 0
    if root is not None:
        altura = 1 + max(height_tree(root["left"]), height_tree(root["right"]))
    return altura

def height(my_rbt):
    altura = 0
    if my_rbt is not None:
        altura = height_tree(my_rbt["root"])
    return altura


# ---------- Rangos ----------

def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        cmp_lo = default_compare(key_initial, root)
        cmp_hi = default_compare(key_final, root)
        if cmp_lo < 0:
            keys_range(root["left"], key_initial, key_final, list_key)
        if cmp_lo <= 0 and cmp_hi >= 0:
            sl.add_last(list_key, rn.get_key(root))
        if cmp_hi > 0:
            keys_range(root["right"], key_initial, key_final, list_key)
    return list_key

def keys(my_rbt, key_initial, key_final):
    lista = sl.new_list()
    if my_rbt is not None:
        keys_range(my_rbt["root"], key_initial, key_final, lista)
    return lista

def values_range(root, key_initial, key_final, list_values):
    if root is not None:
        cmp_lo = default_compare(key_initial, root)
        cmp_hi = default_compare(key_final, root)
        if cmp_lo < 0:
            values_range(root["left"], key_initial, key_final, list_values)
        if cmp_lo <= 0 and cmp_hi >= 0:
            sl.add_last(list_values, rn.get_value(root))
        if cmp_hi > 0:
            values_range(root["right"], key_initial, key_final, list_values)
    return list_values

def values(my_rbt, key_initial, key_final):
    lista = sl.new_list()
    if my_rbt is not None:
        values_range(my_rbt["root"], key_initial, key_final, lista)
    return lista
from DataStructures.Tree import rbt_node as rn


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
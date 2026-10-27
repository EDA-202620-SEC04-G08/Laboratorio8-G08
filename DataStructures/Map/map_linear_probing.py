from DataStructures.List import array_list as lt
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random


def new_map (num_elements, load_factor, prime=109345121):
    capacidad = mf.next_prime(int(num_elements / load_factor))
    
    lista = lt.new_list()
    for i in range(capacidad):
        lt.add_last(lista, me.new_map_entry(None,None))

    rta = {"prime": prime,
           "capacity": capacidad,
           "scale": random.randint(1, prime - 1),
            "shift": random.randint(0, prime - 1),
            "table":lista,
            "current_factor": 0,
            "limit_factor": load_factor,
            "size": 0

    }
    return rta

def rehash (my_map):
    old_table = my_map['table']
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    
    new_table = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(new_table,me.new_map_entry(None,None))
        
    my_map['capacity'] = new_capacity
    my_map["size"] = 0
    my_map['table'] = new_table
    my_map['current_factor'] = 0.0

    for i in range(lt.size(old_table)):
        entrada = lt.get_element(old_table,i)
        llave = me.get_key(entrada)
        valor_llave = me.get_value(entrada)
        if llave is not None and llave != "__EMPTY__":
            put(my_map,llave,valor_llave)
    return my_map

def is_available (table, pos):
    entry = lt.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
    return False

def default_compare(key, entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def put(my_map, key, value):
    hash_pos = mf.hash_value (my_map , key)
    encontrado, posicion = find_slot(my_map, key, hash_pos)

    entrada = lt.get_element(my_map["table"],posicion)
    if encontrado == True:
        me.set_value(entrada, value)
    else:
        me.set_key(entrada,key)
        me.set_value(entrada,value)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"]/my_map["capacity"]
        
        if my_map["current_factor"]>my_map["limit_factor"]:
            rehash(my_map)
    return my_map

def get(my_map, key):
    posicion_hash = mf.hash_value(my_map,key)
    encontrado, posicion = find_slot(my_map,key,posicion_hash)
    if encontrado==True:
        entrada = lt.get_element(my_map["table"],posicion)
        elemento = me.get_value(entrada)
    else:
        elemento = None
    return elemento

def contains(my_map, key):
    posicion_hash = mf.hash_value(my_map,key)
    encontrado, posicion = find_slot(my_map, key, posicion_hash)
    return encontrado

def remove(my_map,key):
    posicion_hash = mf.hash_value(my_map,key)
    encontrado, posicion = find_slot(my_map, key, posicion_hash)
    if encontrado == True:
        entrada = lt.get_element(my_map["table"],posicion)
        me.set_key(entrada,"__EMPTY__" )
        me.set_value(entrada, "__EMPTY__")        
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map["table"]

def size(my_map):
    tamano = my_map["size"]
    return tamano

def is_empty(my_map):
    if my_map["size"] == 0:
        vacio = True
    else:
        vacio = False
    return vacio

def key_set(my_map):
    lista_llaves = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entrada = lt.get_element(my_map["table"],i)
        llave = me.get_key(entrada)
        if llave is not None and llave != "__EMPTY__":
            lt.add_last(lista_llaves, llave)
    return lista_llaves

def value_set(my_map):
    lista_values = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entrada = lt.get_element(my_map["table"],i)
        llave = me.get_key(entrada)
        if llave is not None and llave != "__EMPTY__":
            value = me.get_value(entrada)
            lt.add_last(lista_values, value)
    return lista_values
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as lt
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random

def new_map(num_elements, load_factor, prime=109345121):
    tabla = lt.new_list()
    capacidad = mf.next_prime(int(num_elements / load_factor))
    for i in range(capacidad):
        lt.add_last(tabla, sl.new_list())
    
    mapa = {"prime": prime,
               "capacity": capacidad,
               "scale": random.randint(1, prime - 1),
                "shift": random.randint(0, prime - 1),
                "table":tabla,
                "current_factor": 0,
                "limit_factor": load_factor,
                "size": 0}
    return mapa

def default_compare(key, entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def rehash (my_map):
    old_table = my_map['table']
    new_capacity = mf.next_prime(my_map["capacity"]*2)
    
    new_table = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(new_table,sl.new_list())
          
    my_map['capacity'] = new_capacity
    my_map["size"] = 0
    my_map['table'] = new_table
    my_map['current_factor'] = 0.0

    for i in range(lt.size(old_table)):
        lista = lt.get_element(old_table, i)
        for j in range(sl.size(lista)):
            entrada = sl.get_element(lista, j)
            llave = me.get_key(entrada)
            valor = me.get_value(entrada)
            put(my_map, llave, valor)
    return my_map

def put(my_map, key, value):
    hash_pos = mf.hash_value (my_map , key)
    lista = lt.get_element(my_map["table"],hash_pos)
    
    encontrado = False
    i=0
    while i< sl.size(lista) and encontrado==False:
        entrada = sl.get_element(lista,i)
        if default_compare(key,entrada)==0:
            encontrado = True
            me.set_value(entrada, value)
        i+=1      
    if encontrado == False:
        nueva_entrada = me.new_map_entry(key,value)
        sl.add_last(lista,nueva_entrada)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)
    return my_map

def contains(my_map,key):
    hash_pos = mf.hash_value (my_map , key)
    lista = lt.get_element(my_map["table"],hash_pos)
    encontrado = False
    i=0
    while i< sl.size(lista) and encontrado==False:
        entrada = sl.get_element(lista,i)
        if default_compare(key,entrada)==0:
            encontrado = True
        i+=1      
    return encontrado

def get(my_map,key):
    hash_pos = mf.hash_value (my_map , key)
    lista = lt.get_element(my_map["table"],hash_pos)
    encontrado = False
    i=0
    value = None
    while i< sl.size(lista) and encontrado==False:
        entrada = sl.get_element(lista,i)
        if default_compare(key,entrada)==0:
            encontrado = True
            value = me.get_value(entrada)
        i+=1 
    return value

def remove(my_map,key):
    hash_pos = mf.hash_value (my_map , key)
    lista = lt.get_element(my_map["table"],hash_pos)
    encontrado = False
    i=0
    while i< sl.size(lista) and encontrado==False:
        entrada = sl.get_element(lista,i)
        if default_compare(key,entrada)==0:
            encontrado = True    
            sl.delete_element(lista,i)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        i+=1      
    return my_map

def size(my_map):
    tamano = my_map["size"]
    return tamano

def is_empty(my_map):
    vacio=False
    if my_map["size"]==0:
        vacio=True
    return vacio

def key_set(my_map):
    lista_llaves = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        lista = lt.get_element(my_map["table"],i)
        for j in range(sl.size(lista)):
            entrada = sl.get_element(lista,j)
            llave = me.get_key(entrada)
            lt.add_last(lista_llaves, llave)
    return lista_llaves

def value_set(my_map):
    lista_values = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        lista = lt.get_element(my_map["table"],i)
        for p in range(sl.size(lista)):
            entrada = sl.get_element(lista,p)
            valor = me.get_value(entrada)
            lt.add_last(lista_values, valor)
    return lista_values
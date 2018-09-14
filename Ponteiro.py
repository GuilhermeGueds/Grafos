import ctypes


x = [0,1,2,3]


z = ctypes.cast( id(x), ctypes.py_object ).value   # z obtem o valor que aponta para x
z.append(4)
 # atualiza o x

print(x)   # fail atualizaçao
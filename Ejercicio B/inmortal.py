
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 

print(yang) 
print(yang is yin.yang)

del(yang)
print("?")


def respuesta():
    '''
    El mensaje de "Yang destruido" aparece despues del signo de interrogacion porque el objeto yang todavia esta siendo
    referenciado por el atributo yang del objeto yin. 
    Cuando se llama a del(yang), solo se eliminaria la referencia a yang en el ambito local,
    pero no en el objeto en si.
    El objeto Yang solo se eliminara por completo cuando no haya referencias a el.

    Para que el mensaje "Yang destruido" aparezca antes del signo de interrogacion,
    puedes eliminar tambien la referencia al objeto Yang en el atributo yang del objeto yin,
    antes de imprimir el signo de interrogacion. 
    '''
    print()
    print('De esta manera el mensaje de "Yang destruido" aprace antes de la interrogacion y queda completamente eliminado:')
    del(yin.yang)
    print('?')


respuesta()

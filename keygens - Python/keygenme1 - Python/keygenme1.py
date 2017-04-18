
""" Keygen hecho por AbelJM para el Keygenme1 Scarlett johanson de SoftdatCLS """


dic1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic2 = "AHyukjsdfkjsdfnPQU5xWERY67345aq9nFyR"
dic3 = "o3zYzaI1982Tv2FasgjkkjhkjlJt5Dpe32Ax"
serial = []  """  iniciamos variable donde guardara serial""" 
nombre = raw_input("") """  ingresaremos datos por el teclado""" 
mayusnombre = nombre.upper() """ ponemos en mayusculas nuestro nombre""" 
largo = len(mayusnombre)
"""  largo de el nombre q es ahora mayusnombre""" 
if largo < 3: """  condicion minimo tres letras""" 
    print "minimo tres letras"
else:
    n = 0 """  nos servira para el bucle while""" 
    i = 0 """  recorrera los caracteres""" 
    salto = 0 """ servira para alternar dic2 y dic3 """ 
    while largo > n : """ usamos while ya q el for solo es para recorrer elementos""" 
"""  largo se ira reduciendo hasta romper el bucle""" 
        if salto == 0:
            posicion = dic1.find(mayusnombre[i]) 
            """buscamos cada caracter en dic1 con el metodo find 
            que nos arrojara la posicion donde se encuentra"""
            if posicion < 0:
            """ si el caracter no se encuentra en dic1 nos arrojara -1""" 
                break """ entonces se rompera el bucle""" 
            nombredic2 = dic3[posicion]
           """  con la posicion q nos arrojo,buscamos en dic3[]""" 
            serial.append(nombredic2) """  con append ,almacenamos todo lo q buscams en nombredic2""" 
            largo = largo - 1 """ estamos 1 a largo para q rompa el bucle""" 
            salto = salto + 1 """ sumamos 1 para q salte en dic2""" 
            i = i + 1 """  sumamos 1 para q recorra el siguiente caracter""" 
        
        else:
            posicion = dic1.find(mayusnombre[i])
            if posicion < 0 : 
          """ si el caracter no se encuentra en dic1 nos arrojara -1""" 
                break """ entonces se rompe bucle""" 
            nombredic2 = dic2[posicion]
            serial.append(nombredic2) """  con append ,almacenamos en serial todo lo q buscamos en nombredic2""" 
            largo = largo - 1 """  restamos 1 para q rompa el bucle while""" 
            salto = salto - 1 """  restamos 1 para q salte en dic3""" 
            i = i + 1 """  sumamos uno para q recorra el siguiente caracter""" 
    
  
    numeros = 0 """ iniciamos variable numeros q guardara la todo el proceso del for""" 
    for l in mayusnombre: 
        xoreado = ord(l) ^ salto 
     """  haremos un xor con "^", ord() nos dara el valor ordinal de cada letra que seria su decimal """ 
        shl = xoreado << 10
      """  la instruccion shl vendria a der "<<"   """ 
        xoreado2 = shl ^ 172937463
        sub = xoreado2 - 666
        numeros = numeros + sub """  numeros contendra el resultado de toda operacion""" 
    print "".join(serial) + "-" + str(numeros) """  imprime serial""" 
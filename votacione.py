conprep=0
conpdemoc=0
congeneral=0
print("*************************************")
print("Bienvenido al sistema de votaciones edicion 2021")
print("**********************************************************")
#nombre=(input("Porfavor, indique su nombre: "))
print("**********************************************************")
#rut=(input("Porfavor, indique su rut o n° de identificacion: "))
print("**********************************************************")
#print("Un gusto sr/a "+str(nombre))
print("A continuacion las opciones presentes en este sistema")
print("*************************************")
print("    *** MENU ****    ")
print("=======================")
print("[1]-> Partido Republicano")
print("[2]-> Partido Democrata")
print("[3]-> Totalizacion de Votos")
print("[4]-> Salir del Sistema")
print("=======================")
opcion=str(input("Seleccione alguna opcion: "))
print("******************************************")
if opcion == '1' or 'Partido Republicano' or 'partido republicano':
    conprep+=1
    congeneral+=1
    print("Voto Registrado")
    #print("Efectuado por "+str(nombre))
    #print("de identificacion "+str(rut))

elif opcion == '2' or 'Partido Democrata' or 'partido democrata':
    conpdemoc+=1
    congeneral+=1
    print("Voto Registrado")
    #print("Efectuado por "+str(nombre))
    #print("de identificacion "+str(rut))

elif opcion == '3' or 'Totalizacion de Votos' or 'totalizacion de votos':
    print("La contabilizacion se vera al final del proceso")

elif opcion == '4' or 'Salir del Sistema' or 'salir del sistema':
    print(" Muchas gracias por participar en este proceso, hasta luego")

else:
    print("La opcion que ingreso no es valida para el sistema pruebe intentando otra vez")


print("*********************************************************************************")
print("La cantidad de votos contados para el Partido Republicano fueron: "+str(conprep))
print("*********************************************************************************")
print("La cantidad de votos contados para el Partido Democrata fueron: "+str(conpdemoc))
print("*********************************************************************************")
print("Votos totales: "+str(congeneral))



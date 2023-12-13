from tabulate import tabulate

def darFormato(lista):
    lista = [dato.rstrip().split(';') for dato in lista]
    return lista

#--cargacsv--#
def cargarCSV(directorio):
    comics = []
    try:
        with open(f'{directorio}', 'rt', encoding='utf-8-sig') as archivo:
            comics = [dato for dato in archivo]
    except:
        print('Error al leer el archivo, intentelo nuevamente.')
    else:
        print('Archivo cargado con exito!')
    finally:
        return comics


#-- Busqueda de paginas --#
def buscarMayorPaginas(comics):
    mayor = ""
    mayornum = int(comics[1][5])
    for i, linea in enumerate(comics[1:]):
        if mayornum < int(linea[5]):
            mayornum = int(linea[5])
            mayor = linea
            indx = i+1
    print(f"El Comic con mas paginas es:\n{mayor[0]} con {mayornum} paginas")
    return indx
def buscarMenorPaginas(comics):
    menor = ""
    menornum= int(comics[1][5])
    for i, linea in enumerate(comics[1:]):
        if menornum > int(linea[5]):
            menornum = int(linea[5])
            menor = linea
            indx = i+1
    print(f"El Comic con menos paginas es:\n{menor[0]} con {menornum} paginas")
    return indx
def buscarPorRango(comics):
    rangoinferior = 0
    rangosuperior = 0
    try:
        while rangoinferior < 1: 
            rangoinferior = int(input("Ingrese el numero minimo de paginas: "))
        while rangosuperior <= rangoinferior:
            rangosuperior = int(input("Ingrese el numero maximo de paginas: "))
    except:
        print('Error, intentelo nuevamente')

    else:    
        listarango = [linea for linea in comics[1:] if rangoinferior <= int(linea[5]) <= rangosuperior]
        if listarango:
            print(f"Comics en el rango de paginas {rangoinferior} a {rangosuperior}:\n")
            for i, comic in enumerate(listarango):
                print(f"{i} - {comic[0]} - {comic[5]} páginas")
            return seleccionarComic(comics, listarango)
        else:
            print("No hay comics en el rango especificado")
#--- Busqueda por año --#
def buscarPorAño(comics):
    rangoinicial = 0
    rangofinal = 0
    try:
        while rangoinicial < 1900: 
            rangoinicial = int(input("Ingrese el rango inicial de años: "))
        while rangofinal <= rangoinicial or rangofinal > 2023:
            rangofinal = int(input("Ingrese el rango final año: "))
    except:
        print('Error, intentelo nuevamente')

    else:    
        listarango = [linea for linea in comics[1:] if rangoinicial <= int(linea[2]) <= rangofinal]
        if listarango:
            print(f"Comics en el rango de años desde {rangoinicial} hasta {rangofinal}:\n")
            for i, comic in enumerate(listarango):
                print(f"{i} - {comic[0]} - {comic[2]}")
            return seleccionarComic(comics, listarango)
        else:
            print("No hay comics en el rango especificado")
#-- Busqueda por autor --#
def busquedaPorAutor(comics):
        autor = ''
        while len(autor) < 3:
            autor = input("Ingrese el autor: ")
        lista = [linea for linea in comics[1:] if autor.lower() in linea[1].lower()]
        if lista:
            print(f"Comics que coinciden con la busqueda de {autor}:\n")
            for i, comic in enumerate(lista):
                print(f"{i} - {comic[0]} - {comic[1]}")
            return seleccionarComic(comics, lista)
        else:
            print("No se encontraron comics para el autor ingresado, intentelo nuevamente.")
#-- Busqueda por autor --#
def busquedaPorGenero(comics):
        genero = ''
        while len(genero) < 3:
            genero = input("Ingrese el género: ")
        lista = [linea for linea in comics[1:] if genero.lower() in linea[4].lower()]
        if lista:
            print(f"Comics que coinciden con la busqueda de {genero}:\n")
            for i, comic in enumerate(lista):
                print(f'{i} - {comic[0]} - {comic[4]}')
            return seleccionarComic(comics, lista)
        else:
            print("No se encontraron comics para el género ingresado, intentelo nuevamente.")

#-- Busqueda por editorial --#
def busquedaPorEditorial(comics):
        editorial = ''
        while len(editorial) < 3:
            editorial = input("Ingrese la editorial: ")
        lista = [linea for linea in comics[1:] if editorial.lower() in linea[3].lower()]
        if lista:
            print(f"Comics que coinciden con la busqueda de {editorial}:\n")
            for i, comic in enumerate(lista):
                print(f"{i} - {comic[0]} - {comic[3]}")
            return seleccionarComic(comics, lista)
        else:
            print("No se encontraron comics que coincidan con la editorial ingresada, inténtelo nuevamente.")


def seleccionarComic(comics, lista):
    while True:
        try:
            num = int(input('Seleccione uno de los comics, -1 para salir: '))
        except:
            print('Error, inténtelo nuevamente')
        else:
            if num == -1:
                break
            else:
                titulo = lista[num][0]
                for i, dato in enumerate(comics):
                    if dato[0] == titulo:
                        return i
                    


def exportarCSV(comics):
    try:
        with open ('C:\\Users\\54224\\Desktop\\TPO\\comicsexportados.csv', 'wt', encoding='utf-8-sig') as archivo:
            for comic in comics:
                comic = ';'.join(comic)+'\n'
                archivo.write(comic)
    except:
        print("Error al exportar el archico CSV")
    else:
        print('Archivo exportado exitosamente')

#-----------------------------------------------------menu-------------------------------------------------------#
def opciones():
    if validacion:
        print("""
1 - Cargar CSV
0 - Salir""")
    else:
        print("""
1 - Cargar CSV
2 - ABM
3 - Exportar CSV
0 - Salir\n""")

def opcionesABM():
    print("""
1 - Agregar comics
2 - Eliminar comics
3 - Modificar comics
0 - Salir\n""")

        
def opcionesPaginas():
    print("""
1 - Comic con menos páginas
2 - Comic con más páginas
3 - Por rango de páginas
0 - Salir\n""")
    

def agregarComic(comics):

    while True:
        titulo = ''
        autor = ''
        añoPublicacion = 0
        editorial = ''
        genero = ''
        cantidadPaginas = 0
        while len(titulo) < 3:
            titulo = input('Ingrese el titulo: ')
        while len(autor) < 3:
            autor = input('Ingrese el autor: ')
        while añoPublicacion < 1900 or añoPublicacion > 2023:
            try:
                añoPublicacion = int(input('Ingrese el año de publicación: '))
            except:
                print('Error, inténtelo nuevamente.')
        while len(editorial) < 3:
            editorial = input('Ingrese la editorial: ')
        while len(genero) < 3:
            genero = input('Ingrese el género: ')
        while cantidadPaginas < 1:
            try:
                cantidadPaginas = int(input('Ingrese la cantidad de páginas: '))
            except:
                print('Error, inténtelo nuevamente.')
        añoPublicacion = str(añoPublicacion)
        cantidadPaginas = str(cantidadPaginas)
        comic = [titulo, autor, añoPublicacion, editorial, genero, cantidadPaginas]
        print(f'El comic a agregar es:{comic}')
        verificacion = input('Estos valores son correctos? S/N: ')
        if verificacion.strip().lower() == 's':
            comics.append(comic)
            appendearCsv('C:\\Users\\54224\\Desktop\\TPO\\comics.csv', comic)
            print('Comic añadido correctamente')
            break
        else:
            print('Descartando..')  

def appendearCsv(directorio, comic):
    try:
        with open(directorio, 'a', encoding='utf-8-sig') as archivo:
                dato = ';'.join(comic) + '\n'
                archivo.write(dato)
    except:
        print('Error al escribir el archivo')
    else:
        print('Comic añadido al CSV')

def borrarComic(comics):
    i = buscarIndice(comics)
    if i == -1 or i == None:
        return None
    else:
        eliminado = comics.pop(i)
        print(f'Se ha eliminado el comic {eliminado}')
        return None

def opcionesModificacion():
    print("""
    1 - Título
    2 - Autor
    3 - Año de publicación
    4 - Editorial
    5 - Genero
    6 - Cantidad de páginas
    0 - Salir\n""")

def cargarString():
    string = ''
    while len(string) < 3:
        string = input('Ingrese el nuevo valor: ')
    return string

def cargarIntPositivo():
    entero = 0
    while entero <= 0:
        try:
            entero = int(input('Ingrese el nuevo valor: '))
        except:
            print('Error inténtelo nuevamente')
        else:
            return entero

    

def modificarComic(comics):
    i = buscarIndice(comics)
    if i == -1 or i == None:
        return None
    else:
        while True:
            opcionesModificacion()
            opc = input('Seleccione el valor a modificar, 0 para salir: ')
            if opc == '0':
                break
            elif opc == '1':
                titulo = cargarString()
                print(f'Se cambió el título {comics[i][0]} por {titulo}')
                comics[i][0] = titulo
            elif opc == '2':
                autor = cargarString()
                print(f'Se cambió el autor {comics[i][1]} por {autor}')
                comics[i][1] = autor
            elif opc == '3':
                anioPublicacion = cargarIntPositivo()
                print(f'Se cambió el año de publicación {comics[i][2]} por {anioPublicacion}')
                comics[i][2] = anioPublicacion
            elif opc == '4':
                editorial = cargarString()
                print(f'Se cambió la editorial {comics[i][3]} por {editorial}')
                comics[i][4] = editorial
            elif opc == '5':
                genero = cargarString()
                print(f'Se cambió el género {comics[i][4]} por {genero}')
                comics[i][4] = genero
            elif opc == '6':
                paginas = cargarIntPositivo()
                print(f'Se cambió la cantidad de páginas {comics[i][5]} por {paginas}')
                comics[i][5] = paginas
            else:
                print('Opción incorrecta inténtelo nuevamente')


                
        


def altaBajaModificacion(comics):
    while True:
        opcionesABM()
        opcion = input('Seleccione una de las opciones: ')
        if opcion == '0':
            break
        elif opcion == '1':
            agregarComic(comics)
        elif opcion == '2':
            borrarComic(comics)
        elif opcion == '3':
            modificarComic(comics)    
        else:
            print('Opción incorrecta inténtelo nuevamente')



def opcionesBusqueda():
    print("""
1 - Ver todos los comics disponibles
2 - Buscar por género
3 - Número de páginas
4 - Autor
5 - Buscar por años
6 - Editorial
0 - Salir\n""")
 
def seleccionPaginas(comics):
    while True:
        opPagina = input('Ingrese una opción :')
        if opPagina == '0':
            break
        elif opPagina == '1':
           return buscarMenorPaginas(comics)
        elif opPagina == '2':
           return buscarMayorPaginas(comics)
        elif opPagina == '3':
           return buscarPorRango(comics)
        else:
            print('Opción incorrecta')
    
def buscarIndice(comics):
    while True:
        opcionesBusqueda()
        opb = input('Ingrese la opción para la busqueda: ')
        if opb == '0':
            print('Saliendo')
            break
        elif opb == '1':
            tabla = tabulate(comics, headers='firstrow', tablefmt='pretty', showindex='always')
            print(tabla)
            try:
                num = int(input('Ingrese el número del comic, -1 para salir: '))
            except:
                print('Error')
            else:
                if num == -1:
                    return num
                else:
                    return num+1
        elif opb == '2':
            num = busquedaPorGenero(comics)
            return num
        elif opb == '3':
            opcionesPaginas()
            num = seleccionPaginas(comics)
            return num                            
        elif opb == '4':
            num = busquedaPorAutor(comics)
            return num
        elif opb == '5':
            num = buscarPorAño(comics)
            return num
        elif opb == '6':
            num = busquedaPorEditorial(comics)
            return num
        else:
            print('Opción incorrecta')
    


def menu():
    global validacion
    validacion = True    
    while True:
        opciones()
        op = input('Seleccione una de las opciones: ')
        if op == '0':
            print('Saliendo del programa...')
            break
        # Cargar CSV
        elif op == '1':
            #directorio = input('Ingrese el directorio: ')
            comics = cargarCSV('C:\\Users\\54224\\Desktop\\TPO\\comics.csv')
            if comics:
                comics = darFormato(comics)
                validacion = False
        # ABM
        elif op == '2' and not validacion:
            altaBajaModificacion(comics)
        #Exportar CSV
        elif op == '3' and not validacion:
            exportarCSV(comics)
        #Salir
        else:
            print('Opción incorrecta, inténtelo nuevamente.')


menu()

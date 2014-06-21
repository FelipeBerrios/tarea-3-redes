from numpy import *

#Se definen las variables para no confundirse al trabajar con indices de las matrices

A,B,C,D,E,F,G,H,I= 0,1,2,3,4,5,6,7,8

#Se crearan 2 archivos para mostrar las matrices
miarchivo=open("tablas.txt","w")
miarchivo3=open("tablas_P3.txt","w")

#Esta funcion Obtiene los vecinos de la matriz pasado, y retorna en una lista
#Se hace basicamente para la salida en el archivo y el formato de las tablas.
def Obtenervecinos(X):
	listavecinos=[]
	for i in range(0,len(vecinos)):
		
		if X==i:
			if i==0:
				listavecinos.append("A")
			elif i==1:
				listavecinos.append("B")
			elif i==2:
				listavecinos.append("C")
			elif i==3:
				listavecinos.append("D")
			elif i==4:
				listavecinos.append("E")
			elif i==5:
				listavecinos.append("F")
			elif i==6:
				listavecinos.append("G")
			elif i==7:
				listavecinos.append("H")
			elif i==8:
				listavecinos.append("I")
			else:
				return "error"
			continue
		if EsVecino(X,i):
			if i==0:
				listavecinos.append("A")
			elif i==1:
				listavecinos.append("B")
			elif i==2:
				listavecinos.append("C")
			elif i==3:
				listavecinos.append("D")
			elif i==4:
				listavecinos.append("E")
			elif i==5:
				listavecinos.append("F")
			elif i==6:
				listavecinos.append("G")
			elif i==7:
				listavecinos.append("H")
			elif i==8:
				listavecinos.append("I")
			else:
				return "error"

	return listavecinos

#Asocia una tabla con su respectivo Indice, devuelve la tabla original

def AsociarTabla(i):
	if i==0:
		return costosA
	elif i==1:
		return costosB
	elif i==2:
		return costosC
	elif i==3:
		return costosD
	elif i==4:
		return costosE
	elif i==5:
		return costosF
	elif i==6:
		return costosG
	elif i==7:
		return costosH
	elif i==8:
		return costosI
	else:
		return "error"



#Funcion para imprimir una lista con las tablas acumuladas, con el formato pedido.
def ImprimirTablas(lista,miarchivo):
	for x in lista:
		for i in range(0,len(x)):
			for j in range(0,len(x[0])):
				print x[i][j],"\t|",
				miarchivo.write(str(x[i][j])+"\t|")
			print
			miarchivo.write("\n")
			#for j in range(0,len(x[0])):
			sep="-"*77
			print sep
			miarchivo.write(sep)
			miarchivo.write("\n")
		print "\n"
		miarchivo.write("\n\n")

#Formatea la tabla para dejar las letras de los routers en la primera fila y primera columna.
def FormatearTabla(tabla,X):
	listatotal=["/","A","B","C","D","E","F","G","H","I"]
	tabla2=array(tabla)
	lista=[]
	listavecinos=Obtenervecinos(X)
	for i in range(0,len(tabla)):
		if not EsVecino(X,i):
			if X==i:
				continue
			lista.append(i)
	tabla2=delete(tabla2,lista,0)
	tablaf=[listatotal]
	aux=[]
	for i in range(0,len(tabla2)):
		aux=[]
		aux.append(listavecinos[i])
		for j in range(0,len(tabla2[0])):
			aux.append(tabla2[i][j])
		tablaf.append(aux)	
	return tablaf

	

#Cuando un vector se actualiza, es enviado a sus vecinos
def EnviarVector(X):
	tabla=AsociarTabla(X)
	for i in range(0,tabla.shape[0]):
		if EsVecino(X,i):
			tabla2=AsociarTabla(i)
			tabla2[X]=tabla[X]


#Asigan los vecinos de un Indice a cierta tabla, para solo trabajar con estos.
def AsignarVecinos(X):
	tabla=AsociarTabla(X)
	for i in range(0,costos.shape[0]):
		if EsVecino(X,i):
			tabla2=AsociarTabla(i)
			tabla[i]=tabla2[i]

#Tabla inicial a partir de la matriz de costos
def CrearTablaNodo(X):
	mitabla=zeros((9,9))
	mitabla=mitabla+float("inf")
	mitabla[X]=costos[X]
	return mitabla

#Se realiza el algoritmo de BellmandFord senialado en las diapos.
def BellmanFord(D):
	destino=AsociarTabla(D)
	for i in range(0,destino.shape[1]):
		min=destino[D][i]
		for j in range(0,destino.shape[0]):
			if EsVecino(D,j):
				aux=destino[D][j]+ destino[j][i]
				if aux<min:
					min=aux
		destino[D][i]=min	



#Funcion que comprueba mediante la tabla vecinos, si 2 Routers son vecinos

def EsVecino(X,Y):
	if(vecinos[X][Y]==1):
		return True
	else:
		return False
#En primer Luegar se crean y rellena las tablas vecinos y costos.
 
vecinos= zeros((9,9))
costos= zeros((9,9))
costos=costos+float("inf")

vecinos[A][B]=1
vecinos[A][G]=1
vecinos[A][I]=1

vecinos[B][A]=1
vecinos[B][C]=1
vecinos[B][E]=1

vecinos[C][B]=1
vecinos[C][D]=1

vecinos[D][C]=1
vecinos[D][E]=1
vecinos[D][F]=1
vecinos[D][I]=1

vecinos[E][B]=1
vecinos[E][D]=1
vecinos[E][F]=1
vecinos[E][I]=1

vecinos[F][D]=1
vecinos[F][E]=1
vecinos[F][H]=1

vecinos[G][A]=1
vecinos[G][H]=1

vecinos[H][F]=1
vecinos[H][G]=1
vecinos[H][I]=1

vecinos[I][A]=1
vecinos[I][D]=1
vecinos[I][E]=1
vecinos[I][H]=1

# Se crea la matriz de costos

costos[A][A]=0
costos[A][B]=1
costos[A][G]=4
costos[A][I]=10

costos[B][B]=0
costos[B][A]=1
costos[B][C]=9
costos[B][E]=8

costos[C][C]=0
costos[C][B]=9
costos[C][D]=2

costos[D][D]=0
costos[D][C]=2
costos[D][E]=9
costos[D][F]=4
costos[D][I]=2

costos[E][E]=0
costos[E][B]=8
costos[E][D]=9
costos[E][F]=2
costos[E][I]=1

costos[F][F]=0
costos[F][D]=4
costos[F][E]=2
costos[F][H]=6

costos[G][G]=0
costos[G][A]=4
costos[G][H]=7

costos[H][H]=0
costos[H][F]=6
costos[H][G]=7
costos[H][I]=3

costos[I][I]=0
costos[I][A]=10
costos[I][D]=2
costos[I][E]=1
costos[I][H]=3

ListaA=[]
ListaB=[]
ListaC=[]
ListaD=[]
ListaE=[]
ListaF=[]
ListaG=[]
ListaH=[]
ListaI=[]

costosA= CrearTablaNodo(A)
costosB= CrearTablaNodo(B)
costosC= CrearTablaNodo(C)
costosD= CrearTablaNodo(D)
costosE= CrearTablaNodo(E)
costosF= CrearTablaNodo(F)
costosG= CrearTablaNodo(G)
costosH= CrearTablaNodo(H)
costosI= CrearTablaNodo(I)

#En las listas de cada router se muestra la progresion de cada tabla

ListaA.append(FormatearTabla(array(costosA),A))
ListaB.append(FormatearTabla(array(costosB),B))
ListaC.append(FormatearTabla(array(costosC),C))
ListaD.append(FormatearTabla(array(costosD),D))
ListaE.append(FormatearTabla(array(costosE),E))
ListaF.append(FormatearTabla(array(costosF),F))
ListaG.append(FormatearTabla(array(costosG),G))
ListaH.append(FormatearTabla(array(costosH),H))
ListaI.append(FormatearTabla(array(costosI),I))

#costo anterior maneja la matriz de costos antes de aplicar bellmanford, para ver si cambio en algo su vector director.
costosAanterior= array(costosA)
costosBanterior= array(costosB)
costosCanterior= array(costosC)
costosDanterior= array(costosD)
costosEanterior= array(costosE)
costosFanterior= array(costosF)
costosGanterior= array(costosG)
costosHanterior= array(costosH)
costosIanterior= array(costosI)


AsignarVecinos(A)
AsignarVecinos(B)
AsignarVecinos(C)
AsignarVecinos(D)
AsignarVecinos(E)
AsignarVecinos(F)
AsignarVecinos(G)
AsignarVecinos(H)
AsignarVecinos(I)

ListaA.append(FormatearTabla(array(costosA),A))
ListaB.append(FormatearTabla(array(costosB),B))
ListaC.append(FormatearTabla(array(costosC),C))
ListaD.append(FormatearTabla(array(costosD),D))
ListaE.append(FormatearTabla(array(costosE),E))
ListaF.append(FormatearTabla(array(costosF),F))
ListaG.append(FormatearTabla(array(costosG),G))
ListaH.append(FormatearTabla(array(costosH),H))
ListaI.append(FormatearTabla(array(costosI),I))

#se itera consecutivamente hasta que todas las matrices no cambien.

cambio=9


while cambio>0:
	cambio=0
	#si son distintas, quiere decir que un vector cambio y se debe recomputar con BF.
	if not array_equal(costosAanterior,costosA):
		costosAanterior=array(costosA)
		BellmanFord(A)
		cambio+=1
	if not array_equal(costosBanterior,costosB):
		costosBanterior=array(costosB)
		BellmanFord(B)
		cambio+=1
	if not array_equal(costosCanterior,costosC):
		costosCanterior=array(costosC)
		BellmanFord(C)
		cambio+=1
	if not array_equal(costosDanterior,costosD):
		costosDanterior=array(costosD)
		BellmanFord(D)
		cambio+=1
	if not array_equal(costosEanterior,costosE):
		costosEanterior=array(costosE)
		BellmanFord(E)
		cambio+=1
	if not array_equal(costosFanterior,costosF):
		costosFanterior=array(costosF)
		BellmanFord(F)
		cambio+=1
	if not array_equal(costosGanterior,costosG):
		costosGanterior=array(costosG)
		BellmanFord(G)
		cambio+=1
	if not array_equal(costosHanterior,costosH):
		costosHanterior=array(costosH)
		BellmanFord(H)
		cambio+=1
	if not array_equal(costosIanterior,costosI):
		costosIanterior=array(costosI)
		BellmanFord(I)
		cambio+=1

	#Se adieren las tablas a la lista.
	if cambio!=0:
		ListaA.append(FormatearTabla(array(costosA),A))
		ListaB.append(FormatearTabla(array(costosB),B))
		ListaC.append(FormatearTabla(array(costosC),C))
		ListaD.append(FormatearTabla(array(costosD),D))
		ListaE.append(FormatearTabla(array(costosE),E))
		ListaF.append(FormatearTabla(array(costosF),F))
		ListaG.append(FormatearTabla(array(costosG),G))
		ListaH.append(FormatearTabla(array(costosH),H))
		ListaI.append(FormatearTabla(array(costosI),I))

	#Si cambia e vector director de esa matriz, se debe indicar a los vecinos para que ellos recomputen su propio vector director

	if not array_equal(costosAanterior[A],costosA[A]):
		costosAanterior[A]=costosA[A]
		EnviarVector(A)

	if not array_equal(costosBanterior[B],costosB[B]):
		costosBanterior[B]=costosB[B]
		EnviarVector(B)

	if not array_equal(costosCanterior[C],costosC[C]):
		costosCanterior[C]=costosC[C]
		EnviarVector(C)

	if not array_equal(costosDanterior[D],costosD[D]):
		costosDanterior[D]=costosD[D]
		EnviarVector(D)

	if not array_equal(costosEanterior[E],costosE[E]):
		costosEanterior[E]=costosE[E]
		EnviarVector(E)

	if not array_equal(costosFanterior[F],costosF[F]):
		costosFanterior[F]=costosF[F]
		EnviarVector(F)

	if not array_equal(costosGanterior[G],costosG[G]):
		costosGanterior[G]=costosG[G]
		EnviarVector(G)

	if not array_equal(costosHanterior[H],costosH[H]):
		costosHanterior[H]=costosH[H]
		EnviarVector(H)

	if not array_equal(costosIanterior[I],costosI[I]):
		costosIanterior[I]=costosI[I]
		EnviarVector(I)

#Se imprime en Consola y en un archivo las respectivas matrices
print "Tabla Router A:\n"
miarchivo.write("Tabla Router A:\n\n")
ImprimirTablas(ListaA,miarchivo)

print "Tabla Router B:\n"
miarchivo.write("Tabla Router B:\n\n")
ImprimirTablas(ListaB,miarchivo)

print "Tabla Router C:\n"
miarchivo.write("Tabla Router C:\n\n")
ImprimirTablas(ListaC,miarchivo)

print "Tabla Router D:\n"
miarchivo.write("Tabla Router D:\n\n")
ImprimirTablas(ListaD,miarchivo)

print "Tabla Router E:\n"
miarchivo.write("Tabla Router E:\n\n")
ImprimirTablas(ListaE,miarchivo)

print "Tabla Router F:\n"
miarchivo.write("Tabla Router F:\n\n")
ImprimirTablas(ListaF,miarchivo)

print "Tabla Router G:\n"
miarchivo.write("Tabla Router G:\n\n")
ImprimirTablas(ListaG,miarchivo)

print "Tabla Router H:\n"
miarchivo.write("Tabla Router H:\n\n")
ImprimirTablas(ListaH,miarchivo)

print "Tabla Router I:\n"
miarchivo.write("Tabla Router I:\n\n")
ImprimirTablas(ListaI,miarchivo)



#Pregunta 3
#Aqui basicamente se pide recalcular los costos si desaparece el enlace entre H e I

#Ya no son vecinos
vecinos[H][I]=0
vecinos[I][H]=0

#No hay costo asociado
costos[H][I]=float("inf")
costos[I][H]=float("inf")

costosA= CrearTablaNodo(A)
costosB= CrearTablaNodo(B)
costosC= CrearTablaNodo(C)
costosD= CrearTablaNodo(D)
costosE= CrearTablaNodo(E)
costosF= CrearTablaNodo(F)
costosG= CrearTablaNodo(G)
costosH= CrearTablaNodo(H)
costosI= CrearTablaNodo(I)

#Se realiza un proceso similar al anterior
costosAanterior= array(costosA)
costosBanterior= array(costosB)
costosCanterior= array(costosC)
costosDanterior= array(costosD)
costosEanterior= array(costosE)
costosFanterior= array(costosF)
costosGanterior= array(costosG)
costosHanterior= array(costosH)
costosIanterior= array(costosI)




AsignarVecinos(A)
AsignarVecinos(B)
AsignarVecinos(C)
AsignarVecinos(D)
AsignarVecinos(E)
AsignarVecinos(F)
AsignarVecinos(G)
AsignarVecinos(H)
AsignarVecinos(I)


ListaA3=[]
ListaB3=[]
ListaC3=[]
ListaD3=[]
ListaE3=[]
ListaF3=[]
ListaG3=[]
ListaH3=[]
ListaI3=[]


cambio=9


while cambio>0:
	cambio=0
	if not array_equal(costosAanterior,costosA):
		costosAanterior=array(costosA)
		BellmanFord(A)
		cambio+=1
	if not array_equal(costosBanterior,costosB):
		costosBanterior=array(costosB)
		BellmanFord(B)
		cambio+=1
	if not array_equal(costosCanterior,costosC):
		costosCanterior=array(costosC)
		BellmanFord(C)
		cambio+=1
	if not array_equal(costosDanterior,costosD):
		costosDanterior=array(costosD)
		BellmanFord(D)
		cambio+=1
	if not array_equal(costosEanterior,costosE):
		costosEanterior=array(costosE)
		BellmanFord(E)
		cambio+=1
	if not array_equal(costosFanterior,costosF):
		costosFanterior=array(costosF)
		BellmanFord(F)
		cambio+=1
	if not array_equal(costosGanterior,costosG):
		costosGanterior=array(costosG)
		BellmanFord(G)
		cambio+=1
	if not array_equal(costosHanterior,costosH):
		costosHanterior=array(costosH)
		BellmanFord(H)
		cambio+=1
	if not array_equal(costosIanterior,costosI):
		costosIanterior=array(costosI)
		BellmanFord(I)
		cambio+=1

	if cambio==0:
		ListaA3.append(FormatearTabla(array(costosA),A))
		ListaB3.append(FormatearTabla(array(costosB),B))
		ListaC3.append(FormatearTabla(array(costosC),C))
		ListaD3.append(FormatearTabla(array(costosD),D))
		ListaE3.append(FormatearTabla(array(costosE),E))
		ListaF3.append(FormatearTabla(array(costosF),F))
		ListaG3.append(FormatearTabla(array(costosG),G))
		ListaH3.append(FormatearTabla(array(costosH),H))
		ListaI3.append(FormatearTabla(array(costosI),I))

	if not array_equal(costosAanterior[A],costosA[A]):
		costosAanterior[A]=costosA[A]
		EnviarVector(A)

	if not array_equal(costosBanterior[B],costosB[B]):
		costosBanterior[B]=costosB[B]
		EnviarVector(B)

	if not array_equal(costosCanterior[C],costosC[C]):
		costosCanterior[C]=costosC[C]
		EnviarVector(C)

	if not array_equal(costosDanterior[D],costosD[D]):
		costosDanterior[D]=costosD[D]
		EnviarVector(D)

	if not array_equal(costosEanterior[E],costosE[E]):
		costosEanterior[E]=costosE[E]
		EnviarVector(E)

	if not array_equal(costosFanterior[F],costosF[F]):
		costosFanterior[F]=costosF[F]
		EnviarVector(F)

	if not array_equal(costosGanterior[G],costosG[G]):
		costosGanterior[G]=costosG[G]
		EnviarVector(G)

	if not array_equal(costosHanterior[H],costosH[H]):
		costosHanterior[H]=costosH[H]
		EnviarVector(H)

	if not array_equal(costosIanterior[I],costosI[I]):
		costosIanterior[I]=costosI[I]
		EnviarVector(I)

#Se imprime la salida de la pregunta 3, con sus respectivas tablas de costos para cada Router.
print "Pregunta 3\n"


print "Tabla Router A:\n"
miarchivo3.write("Tabla Router A:\n\n")
ImprimirTablas(ListaA3,miarchivo3)

print "Tabla Router B:\n"
miarchivo3.write("Tabla Router B:\n\n")
ImprimirTablas(ListaB3,miarchivo3)

print "Tabla Router C:\n"
miarchivo3.write("Tabla Router C:\n\n")
ImprimirTablas(ListaC3,miarchivo3)

print "Tabla Router D:\n"
miarchivo3.write("Tabla Router D:\n\n")
ImprimirTablas(ListaD3,miarchivo3)

print "Tabla Router E:\n"
miarchivo3.write("Tabla Router E:\n\n")
ImprimirTablas(ListaE3,miarchivo3)

print "Tabla Router F:\n"
miarchivo3.write("Tabla Router F:\n\n")
ImprimirTablas(ListaF3,miarchivo3)

print "Tabla Router G:\n"
miarchivo3.write("Tabla Router G:\n\n")
ImprimirTablas(ListaG3,miarchivo3)

print "Tabla Router H:\n"
miarchivo3.write("Tabla Router H:\n\n")
ImprimirTablas(ListaH3,miarchivo3)

print "Tabla Router I:\n"
miarchivo3.write("Tabla Router I:\n\n")
ImprimirTablas(ListaI3,miarchivo3)

miarchivo.close()
miarchivo3.close()
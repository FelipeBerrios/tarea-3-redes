from numpy import *

A,B,C,D,E,F,G,H,I= 0,1,2,3,4,5,6,7,8

def CrearTablaNodo(X):
	mitabla=zeros((9,9))
	mitabla=mitabla+float("inf")
	mitabla[X]=costos[X]
	return mitabla






def EsVecino(X,Y):
	if(vecinos[X][Y]==1):
		return True
	else:
		return False
 
vecinos= zeros((9,9))
costos= zeros((9,9))

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

costos[A][B]=1
costos[A][G]=4
costos[A][I]=10

costos[B][A]=1
costos[B][C]=9
costos[B][E]=8

costos[C][B]=9
costos[C][D]=2

costos[D][C]=2
costos[D][E]=9
costos[D][F]=4
costos[D][I]=2

costos[E][B]=8
costos[E][D]=9
costos[E][F]=2
costos[E][I]=1

costos[F][D]=4
costos[F][E]=2
costos[F][H]=6

costos[G][A]=4
costos[G][H]=7

costos[H][F]=6
costos[H][G]=7
costos[H][I]=3

costos[I][A]=10
costos[I][D]=2
costos[I][E]=1
costos[I][H]=3

costosA= CrearTablaNodo(A)
costosB= CrearTablaNodo(B)
costosC= CrearTablaNodo(C)
costosD= CrearTablaNodo(D)
costosE= CrearTablaNodo(E)
costosF= CrearTablaNodo(F)
costosG= CrearTablaNodo(G)
costosH= CrearTablaNodo(H)
costosI= CrearTablaNodo(I)


print 
import networkx as nx
from matplotlib import pyplot as plt
import math
import os


class Graph_Class:

    def __init__(self):
        self.v = [] # Lista de vectores , conjunto de vertices
        self.a = [] # Lista de aristas , conjunto de aristas
        self.p = [] # Lista de pesos de cada arista
        self.g = nx.DiGraph() #Dibuja el grafo
        self.d = [] # Si es dirigido o no # Lista de direcciones
        self.pox = [] # Lista de las posiciones
        self.ca= [] #Lista de Cabezas
        self.co = [] #lista de Colas
        #self.color = ["orange","red","green"] # Lista de colores , red = Muy afectado , Orange = Masomenos afectado , Green = Esta pasable o controlado
        self.m =[[None]*0 for i in range(0)]#Matriz de peso y adyacencia

    #Primero tenemos la función para ver si se encuentra o no el vertice en el conjunto de vertices
    def is_vertex (self , v):
        if self.v.count(v) == 0:
            return False
        return True
    #Agregar Los vertices
    def add_vertex(self , v , pox):
        if self.is_vertex(v): #Primero revisa si esta el vertice
            return False
        else:
            self.v.append(v) #Si no esta lo agrega a el conjunto
            self.pox.append(pox)
        #Continuamos al agregar el nuevo vertice a la Matriz de adyacencia
        f = c = len(self.m)
        m_aux = [[None]*(f+1) for i in range(c+1)] # Agrega una fila y una columna a la matriz
        # Recorro la matriz para copiar si contenido a la nueva matriz auxiliar
        for n in range(f):
            for k in range(c):
                m_aux[n][k] = self.m[n][k]

        self.m = m_aux
        return True

    #Agregar Arista
    def add_egde (self , Cabeza , Cola , Dirigido , Peso):
        self.d.append(Dirigido)
        if not(self.is_vertex(Cabeza))or not(self.is_vertex(Cola)): # Si no estan El vertice Cabeza y el vertice cola  en el conjunto de vertices , retornara falso
            return False
        else:
            if not Dirigido:
                self.ca.append(Cola)
                self.co.append(Cabeza)
                self.m[self.v.index(Cola)][self.v.index(Cabeza)] = Peso
                u = Cola+Cabeza
                self.a.append(u) #Agregamos la arista a el conjunto de aristas
                self.p.append(Peso) #Agregamos el peso a el conjunto de pesos
            else:
                self.ca.append(Cabeza)
                self.co.append(Cola)
                self.m[self.v.index(Cabeza)][self.v.index(Cola)] = Peso
                u = Cabeza+Cola
                self.a.append(u) #Agregamos la arista a el conjunto de aristas
                self.p.append(Peso) #Agregamos el peso a el conjunto de pesos

        return True

    def print_MatrixP(self , y): #Immprimir la matriz de adyasencia o de peso , Parametro y es la matriz que se quiere imprimir, en un archivo de texto
        file = open("Matriz_adyacencia.txt","w")
        ca = "\n"
        #file.write(ca)
        for b in range(len(y)):
            ca += "\t"+"\t"+ self.v[b]
            #file.write(ca)
        ca += "\n" + ("   ."*len(y))
        #file.write(ca)
        for x in range(len(y)):
            ca += "\n" + self.v[x] + "|"
            #file.write(ca)
            for z in range(len(y)):
                if  x == z and (y[x][z] is None or y[x][z] == 0):
                    ca += "\t" +"\t" + " "+"0"
                    #file.write(ca)
                else:
                    if y[x][z] is None :
                        ca += "\t"+"\t" + "  "+"X"
                        #file.write(ca)
                    elif math.isinf(y[x][z]):
                        ca += "\t" + "="
                        #file.write(ca)
                    else:
                        ca += "\t" + "\t" +str(y[x][z])
                        #file.write(ca)
        ca += "\n"
        file.write(ca)
        file.close()
        #print(ca)

    def _Draw_ (self):
        imData = plt.imread("mapa.png")
        plt.imshow(imData)
        #Dibujar los vertices con su posicion
        for i in range(len(self.v)):
            self.g.add_node(self.v[i],Pos=self.pox[i])
        #Dibujar las aristas con su peso
        for x in range(len(self.ca)):
                self.g.add_edge(self.ca[x],self.co[x], Weight = self.p[x])
        #Dibujar # TODO:
        pos = nx.get_node_attributes(self.g,'Pos')
        #color = nx.get_node_attributes(self.g,'Color')
        nx.draw_networkx(self.g,pos,edge_color='black',node_color='red',node_size=40, font_size=5)
        label = nx.get_edge_attributes(self.g , 'Weight')
        nx.draw_networkx_edge_labels(self.g,pos,edge_labels = label, style='dashed', font_size=5)
        nx.write_edgelist(self.g,'Listadearistas.txt')
        plt.show()
        return True

    def contenido_en(self,lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def recorrido_profundidad(self, inicio):
        if not self.is_vertex(inicio):
            return None

        recorrido = []
        pila = [inicio]
        x = inicio
        #print (pila)

        while len(pila) > 0:
            v_aux = pila.pop()
            #print(v_aux)
            if not self.contenido_en(recorrido, v_aux):
                recorrido.append(v_aux)

            condicion = True

            for i in range(len(self.m)):
                if self.m[self.v.index(v_aux)][i] is not None:
                    v_candidato = self.v[i]
                    #print(v_candidato)

                    # al parecer se puede reemplazar por "and not self.contenido_en(pila, v_candidato)
                    if not self.contenido_en(recorrido, v_candidato) and condicion:
                        f = x+v_candidato
                        if f in self.a:
                            # Es como un Break.
                            condicion = False
                            x = v_candidato
                            pila.append(v_aux)
                            pila.append(v_candidato)

        return recorrido

    #Funcion Dijkstra
    def Dijkstra(self,s,t):
        st = s + t
        #l = [0] # Lista de pesos de s hata t
        L = {}
        S = []
        pe = 0
        #print(st)
        if s != t:
            #print(st)
            L[s]=0
            pp = L[s] # Peso inicial va cambiando
            v = s # vertice que ira cambiando
            for i in self.v:
                if i != s:
                    L[i]=float('inf')
            p = [] #pesos de los adyacentes a s
            #print(L)
            while t not in S:
                #a.Encontrar el de mayor peso entre todos los pesos en L
                pp=0
                v = ""
                for x in L:
                    if x not in S:
                        for w in L:
                            if w not in S:
                                if L[x] >= L[w] and L[w] != float('inf') and  L[x] != float('inf'):
                                    if L[x] >= pp:
                                        pp = L[x]
                                        v = x
                                elif  L[w] >= L[x] and L[w] != float('inf') and  L[x] != float('inf'):
                                    if L[w] >= pp:
                                        pp = L[w]
                                        v = w

                #print(S)
                #print(v)
                S.append(v)
                #c.para todo los vertices que aun no estan en S cambio el peso en el diccionario L
                for f in self.v:
                    if f not in S:
                        k = v+f
                        for i in range(len(self.a)):
                            #print(k)
                            if  k == self.a[i]:
                                max = L[f]
                                #print(max)
                                if max >= pp+self.p[i] and max != float('inf'):
                                    L[f]=max
                                    #print(L[f])
                                elif max <= pp+self.p[i] and  max != float('inf'):
                                    L[f]= pp+self.p[i]
                                    #print(L[f])
                                elif max >= pp+self.p[i] and max == float('inf'):
                                    L[f]= pp+self.p[i]
                                        #print(L[f])
                                    #print(L)
                                elif max <= pp+self.p[i] and max == float('inf'):
                                    L[f]= pp+self.p[i]

            return S , L[t]





    def delete_arista(self,arista):
        r = self.a
        if arista in r:
            r.remove(arista)


    def Corte_aristas(self):
        aristas_corte = []
        for i in self.a:
            self.a.remove(i)
            for e in self.v:
                y = self.recorrido_profundidad(e)
                print("Posible recorrido:")
                print(y)
                if len(y) == 1 and y[0] == e:
                    aristas_corte.append(i)
            self.a.append(i)
                #print("Es conexo")
        if aristas_corte == []:
            print("El grafo no tiene aristas de corte")
        return aristas_corte

    def print_MatrixA(self,x,y):#x lista con vertices , y lista de Aristas
        file=open("MatrisxA.txt","w")
        ca="\n"
        for b in range(len(x)):
            ca+= "\t" + x[b]
            file.write(ca)
        ca+="\n"+("\t"*len(x) + " ")
        for r in range(len(x)):
            ca += "\n" + x[r] + "|"
            for z in range(len(x)):
                #for p in y:
                if str(x[r]+x[z])in y:
                    ca += "\t"  +"1"
                    file.write(ca)
                else:
                    ca+="\t" + "0"

        ca += "\n"
        file.write(ca)
        file.close()

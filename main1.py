from Grafo import *

G = Graph_Class()
dic = {"A":(850,174),"B":(768,66),"C":(775,238),"D":(495,134),"E":(143,158),"F":(493,100),"G":(534,140),"H":(470,102),"I":(483,156),"J":(467,161)
,"K":(531,110),"L":(597,157)  ,"M":(305,359),"N":(129,228),"O":(544,64),"P":(654,222),"Q":(524,128),"R":(203,320),"S":(515,107),"T":(217,358)
,"U":(512,113),"V":(164,79),"W":(684,186)}
for key in dic:
    G.add_vertex(key , dic[key])
    #print( key, ":", dic[key])
#1China
G.add_egde("A","B",True,1500)
G.add_egde("A","D",True,2600)
G.add_egde("A","E",True,2500)
G.add_egde("A","C",True,1531)
G.add_egde("A","G",True,2300)
#2Rusia a otros paises
G.add_egde("B","K",True,2000)
G.add_egde("B","L",True,600)
G.add_egde("B","O",True,700)
G.add_egde("B","N",True,567)
G.add_egde("B","M",True,632)
G.add_egde("B","E",True,897)
G.add_egde("B","J",True,678)
G.add_egde("B","P",True,675)
#3Estados unidos  a Otros
G.add_egde("E","I",True,800)
G.add_egde("E","F",True,700)
G.add_egde("E","M",True,531)
G.add_egde("E","N",True,636)
G.add_egde("E","V",True,600)
G.add_egde("E","S",True,512)
G.add_egde("E","L",True,678)
#4Canada a otros paises
G.add_egde("V","N",True,100)
G.add_egde("V","M",True,2000)
G.add_egde("V","R",True,900)
G.add_egde("V","T",True,633)
G.add_egde("V","C",True,532)
G.add_egde("V","B",True,690)
G.add_egde("V","P",True,988)
#5brasil a otros paises
G.add_egde("M","T",True,500)
G.add_egde("M","R",True,600)
G.add_egde("M","S",True,632)
G.add_egde("M","L",True,765)
G.add_egde("M","C",True,890)
#6Paises bajos
G.add_egde("S","U",True,700)
G.add_egde("S","K",True,950)
G.add_egde("S","O",True,800)
G.add_egde("S","F",True,500)
G.add_egde("S","V",True,897)
G.add_egde("S","P",True,768)
#7Turquia
G.add_egde("L","W",True,1100)
G.add_egde("L","D",True,897)
G.add_egde("L","S",True,789)
G.add_egde("L","P",True,674)
G.add_egde("L","V",True,549)
G.add_egde("L","F",True,987)
#8india
G.add_egde("C","W",True,607)
G.add_egde("C","L",True,600)
G.add_egde("C","P",True,500)
G.add_egde("C","B",True,740)
G.add_egde("C","D",True,599)
G.add_egde("C","U",True,678)
#9Reino unido
G.add_egde("F","H",True,848)
G.add_egde("F","J",True,750)
G.add_egde("F","D",True,600)
G.add_egde("F","E",True,1000)
G.add_egde("F","I",True,1250)
G.add_egde("F","C",True,678)
G.add_egde("F","P",True,970)


#10Francia
G.add_egde("D","G",True,670)
G.add_egde("D","I",True,670)
G.add_egde("D","V",True,670)
G.add_egde("D","I",True,590)
G.add_egde("D","K",True,698)
G.add_egde("D","W",True,786)
#11España
G.add_egde("I","G",True,437)
G.add_egde("I","J",True,238)
G.add_egde("I","E",True,513)
G.add_egde("I","F",True,671)
G.add_egde("I","H",True,671)
G.add_egde("I","M",True,800)
G.add_egde("I","N",True,850)
G.add_egde("I","K",True,678)
G.add_egde("I","W",True,789)
#12Iran
G.add_egde("W","P",True,540)
G.add_egde("W","S",True,604)
G.add_egde("W","Q",True,607)
G.add_egde("W","O",True,578)
G.add_egde("W","F",True,500)
G.add_egde("W","U",True,870)
#13Italia
G.add_egde("G","K",True,630)
G.add_egde("G","S",True,700)
G.add_egde("G","W",True,657)
G.add_egde("G","O",True,900)
G.add_egde("G","F",True,890)
G.add_egde("G","U",True,546)
#14Suiza
G.add_egde("Q","G",True,1300)
G.add_egde("Q","D",True,1200)
G.add_egde("Q","F",True,800)
G.add_egde("Q","P",True,645)
G.add_egde("Q","K",True,740)
G.add_egde("Q","L",True,678)
G.add_egde("Q","N",True,998)
#15Alemania
#G.add_egde("K","D",True,750)
G.add_egde("K","H",True,645)
G.add_egde("K","U",True,860)
G.add_egde("K","M",True,900)
G.add_egde("K","J",True,700)
G.add_egde("K","F",True,654)
#16Belgica
G.add_egde("U","D",True,600)
G.add_egde("U","H",True,700)
G.add_egde("U","O",True,120)
G.add_egde("U","Q",True,500)
G.add_egde("U","I",True,890)
G.add_egde("U","L",True,770)
#17Ecuador
G.add_egde("R","N",True,600)
G.add_egde("R","U",True,568)
G.add_egde("R","L",True,504)
G.add_egde("R","Q",True,630)
G.add_egde("R","B",True,576)
#18Mexico
G.add_egde("N","T",True,1500)
G.add_egde("N","M",True,1000)
G.add_egde("N","F",True,700)
G.add_egde("N","U",True,500)
G.add_egde("N","K",True,874)

#19Suecia
G.add_egde("O","H",True,900)
G.add_egde("O","V",True,700)
G.add_egde("O","J",True,650)
G.add_egde("O","Q",True,845)
G.add_egde("O","N",True,954)
#20Arabia Saudita
G.add_egde("P","L",True,730)
G.add_egde("P","I",True,600)
G.add_egde("P","E",True,300)
G.add_egde("P","O",True,789)
G.add_egde("P","N",True,890)
G.add_egde("P","T",True,897)
G.add_egde("P","R",True,603)
#21Peru
G.add_egde("T","E",True,900)
G.add_egde("T","P",True,800)
G.add_egde("T","B",True,850)
G.add_egde("T","R",True,850)
G.add_egde("T","H",True,767)
#22Irlanda
G.add_egde("H","E",True,500)
G.add_egde("H","J",True,700)
G.add_egde("H","B",True,700)
G.add_egde("H","P",True,609)
G.add_egde("H","N",True,676)
#23portugal
G.add_egde("J","M",True,600)
G.add_egde("J","D",True,706)
G.add_egde("J","T",True,540)
G.add_egde("J","G",True,800)
G.add_egde("J","S",True,709)
#print(G.ca)
#print(G.co)
#print(G.a)
#print(G.p)
G.print_MatrixP(G.m)
G._Draw_()





#Ejecución del Dijkstra
S , t  = G.Dijkstra("A","R")
print("El recorrido del virus fue:")
print(S)
Prueba = Graph_Class()
newdic = {}
for g in S:
    for h in range(len(G.v)):
        if g ==G.v[h]:
            newdic[g]=G.pox[h]
#print(newdic)
for key in newdic:
    Prueba.add_vertex(key , newdic[key])
while(len(S)>1):
    cd = S[0]+S[1]
    if cd in G.a:
        for r in range(len(G.a)):
                if cd == G.a[r]:
                    #print(cd)
                    #print(G.a[r])
                    Prueba.add_egde(S[0],S[1],True,G.p[r])
                    S.pop(0)
t = str(t)
print("Cantidad de infectados: " + t)
Prueba._Draw_()

#G.print_MatrixA(G.v,G.a)
#G.delete_arista("RU")
#G.Dijkstra("A","T")

print(G.recorrido_profundidad("V"))
#G._Draw_()

G.Corte_aristas()
